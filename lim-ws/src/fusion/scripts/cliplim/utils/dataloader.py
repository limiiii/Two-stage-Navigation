import os

import cv2
import numpy as np
import torch
import torch.utils.data as data
from PIL import Image

from .utils import cvtColor, preprocess_input, pre_caption
from .utils_aug import CenterCrop, ImageNetPolicy, RandomResizedCrop, Resize


class ClipDataset(data.Dataset):
    def __init__(self, input_shape, lines, datasets_path, random, autoaugment_flag=True):
        self.input_shape    = input_shape
        self.lines          = lines

        self.random         = random
        self.datasets_path  = datasets_path

        self.text       = []
        self.image      = []
        self.depth_image= []
        self.txt2img    = {}
        self.img2txt    = {}
        txt_id          = 0
        #遍历获取标签文件中的 深度图名称、图像名称、标签内容，并分别存储在self.image和self.text列表中
        for img_id, ann in enumerate(self.lines):
            self.depth_image.append(ann['depth_image'])
            self.image.append(ann['image'])
            self.img2txt[img_id] = []
            for i, caption in enumerate(ann['caption']):
                #将标签语句中无关的字符全部删除，并保证语句长度不超过77
                self.text.append(pre_caption(caption, 77))
                self.img2txt[img_id].append(txt_id)
                self.txt2img[txt_id] = img_id
                txt_id += 1

        self.autoaugment_flag   = autoaugment_flag
        if self.autoaugment_flag:
            self.resize_crop = RandomResizedCrop(input_shape)
            self.policy      = ImageNetPolicy()

            #使用插值缩放的方法使图片的高宽均大于input_shape,然后通过裁剪中心得到大小符合的图片
            self.resize      = Resize(input_shape[0] if input_shape[0] == input_shape[1] else input_shape)
            self.center_crop = CenterCrop(input_shape)
        
    def __len__(self):
        #返回数据集的数量，json文件存放一个大列表，其中每个数据对应一个字典，字典中存储深度图路径、图片路径、和标签
        return len(self.lines)

    def rand(self, a=0, b=1):
        return np.random.rand()*(b-a) + a

    def __getitem__(self, index):
        # 1.随机选择当前图片对应的任意一个语句作为其标签（因为图片和caption为一对多的关系）
        caption = self.text[np.random.choice(self.img2txt[index])]

        # 2.读取图片，并转换成RGB图像
        photo_name  = self.image[index]
        image_path  = os.path.join(self.datasets_path, photo_name)
        image = Image.open(image_path)
        image = cvtColor(image)
        #对读取的图片进行插值补足尺寸、再进行裁剪和进行数据增强
        if self.autoaugment_flag:
            image = self.AutoAugment(image, random=self.random)
        else:
            image = self.get_random_data(image, self.input_shape, random=self.random)
        image = np.transpose(preprocess_input(np.array(image, dtype='float32')), (2, 0, 1))

        # 3.读取深度图片，并转换成RGB图像
        depth_photo_name = self.depth_image[index]
        depth_image_path = os.path.join(self.datasets_path, depth_photo_name)
        depth_image = Image.open(depth_image_path)
        depth_image = cvtColor(depth_image)
        # 对读取的图片进行插值补足尺寸、再进行裁剪和进行数据增强
        if self.autoaugment_flag:
            depth_image = self.AutoAugment(depth_image, random=self.random)
        else:
            depth_image = self.get_random_data(depth_image, self.input_shape, random=self.random)
        depth_image = np.transpose(preprocess_input(np.array(depth_image, dtype='float32')), (2, 0, 1))

        return image, caption, depth_image

    def get_random_data(self, image, input_shape, jitter=.3, hue=.1, sat=0.7, val=0.3, random=True):
        #------------------------------#
        #   获得图像的高宽与目标高宽
        #------------------------------#
        iw, ih  = image.size
        h, w    = input_shape

        if not random:
            scale = min(w/iw, h/ih)
            nw = int(iw*scale)
            nh = int(ih*scale)
            dx = (w-nw)//2
            dy = (h-nh)//2

            #---------------------------------#
            #   将图像多余的部分加上灰条
            #---------------------------------#
            image       = image.resize((nw,nh), Image.BICUBIC)
            new_image   = Image.new('RGB', (w,h), (128,128,128))
            new_image.paste(image, (dx, dy))
            image_data  = np.array(new_image, np.float32)

            return image_data

        #------------------------------------------#
        #   对图像进行缩放并且进行长和宽的扭曲
        #------------------------------------------#
        new_ar = iw/ih * self.rand(1-jitter,1+jitter) / self.rand(1-jitter,1+jitter)
        scale = self.rand(0.75, 1.5)
        if new_ar < 1:
            nh = int(scale*h)
            nw = int(nh*new_ar)
        else:
            nw = int(scale*w)
            nh = int(nw/new_ar)
        image = image.resize((nw,nh), Image.BICUBIC)

        #------------------------------------------#
        #   将图像多余的部分加上灰条
        #------------------------------------------#
        dx = int(self.rand(0, w-nw))
        dy = int(self.rand(0, h-nh))
        new_image = Image.new('RGB', (w,h), (128, 128, 128))
        new_image.paste(image, (dx, dy))
        image = new_image

        #------------------------------------------#
        #   翻转图像
        #------------------------------------------#
        flip = self.rand()<.5
        if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        rotate = self.rand()<.5
        if rotate: 
            angle = np.random.randint(-15,15)
            a,b = w/2,h/2
            M = cv2.getRotationMatrix2D((a,b),angle,1)
            image = cv2.warpAffine(np.array(image), M, (w,h), borderValue=[128, 128, 128]) 

        image_data      = np.array(image, np.uint8)
        #---------------------------------#
        #   对图像进行色域变换
        #   计算色域变换的参数
        #---------------------------------#
        r               = np.random.uniform(-1, 1, 3) * [hue, sat, val] + 1
        #---------------------------------#
        #   将图像转到HSV上
        #---------------------------------#
        hue, sat, val   = cv2.split(cv2.cvtColor(image_data, cv2.COLOR_RGB2HSV))
        dtype           = image_data.dtype
        #---------------------------------#
        #   应用变换
        #---------------------------------#
        x       = np.arange(0, 256, dtype=r.dtype)
        lut_hue = ((x * r[0]) % 180).astype(dtype)
        lut_sat = np.clip(x * r[1], 0, 255).astype(dtype)
        lut_val = np.clip(x * r[2], 0, 255).astype(dtype)

        image_data = cv2.merge((cv2.LUT(hue, lut_hue), cv2.LUT(sat, lut_sat), cv2.LUT(val, lut_val)))
        image_data = cv2.cvtColor(image_data, cv2.COLOR_HSV2RGB)
        return image_data
        
    def AutoAugment(self, image, random=True):
        if not random:
            image = self.resize(image)
            image = self.center_crop(image)
            return image
        #------------------------------------------#
        #   resize并且随即裁剪
        #------------------------------------------#
        image = self.resize_crop(image)
        
        #------------------------------------------#
        #   翻转图像
        #------------------------------------------#
        flip = self.rand()<.5
        if flip: image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        #------------------------------------------#
        #   随机增强
        #------------------------------------------#
        image = self.policy(image)
        return image
            

def dataset_collate(batch):
    images      = []
    captions    = []
    depth_images= []
    for image, caption, depth_image in batch:
        images.append(image)
        captions.append(caption)
        depth_images.append(depth_image)
        
    images      = torch.from_numpy(np.array(images)).type(torch.FloatTensor)
    depth_images = torch.from_numpy(np.array(depth_images)).type(torch.FloatTensor)
    return images, captions, depth_images