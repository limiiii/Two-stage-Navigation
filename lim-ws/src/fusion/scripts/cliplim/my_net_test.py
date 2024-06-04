import torch
from torchvision import transforms
from pkg_resources import packaging
from nets.clip import CLIP
from typing import Any, Union, List
from PIL import Image
import numpy as np
from utils.utils import get_configs
from utils.utils_aug import resize, center_crop
from nets.simple_tokenizer import SimpleTokenizer as _Tokenizer, tokenize

if packaging.version.parse(torch.__version__) < packaging.version.parse("1.7.1"):
    warnings.warn("PyTorch version 1.7.1 or higher is recommended")

#---------------------------------------------------#
#   对输入图像进行resize
#---------------------------------------------------#
def preprocess(image, size):
    w, h = size
    iw, ih = image.size
    if(iw >= w and ih >= h):
        letterbox_image = False
    else:
        letterbox_image = True
    if letterbox_image:
        '''resize image with unchanged aspect ratio using padding'''
        scale = min(w/iw, h/ih)
        nw = int(iw*scale)
        nh = int(ih*scale)

        image = image.resize((nw,nh), Image.BICUBIC)
        new_image = Image.new('RGB', size, (128,128,128))
        new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    else:
        if h == w:
            new_image = resize(image, h)
        else:
            new_image = resize(image, [h ,w])
        new_image = center_crop(new_image, [h ,w])
    return new_image

def tokenize(texts: Union[str, List[str]], context_length: int = 77, truncate: bool = False) -> Union[torch.IntTensor, torch.LongTensor]:
    if isinstance(texts, str):
        texts = [texts]
    _tokenizer = _Tokenizer()
    sot_token = _tokenizer.encoder["<|startoftext|>"]
    eot_token = _tokenizer.encoder["<|endoftext|>"]
    all_tokens = [[sot_token] + _tokenizer.encode(text) + [eot_token] for text in texts]
    if packaging.version.parse(torch.__version__) < packaging.version.parse("1.8.0"):
        result = torch.zeros(len(all_tokens), context_length, dtype=torch.long)
    else:
        result = torch.zeros(len(all_tokens), context_length, dtype=torch.int)
    for i, tokens in enumerate(all_tokens):
        if len(tokens) > context_length:
            if truncate:
                tokens = tokens[:context_length]
                tokens[-1] = eot_token
            else:
                raise RuntimeError(f"Input {texts[i]} is too long for context length {context_length}")
        result[i, :len(tokens)] = torch.tensor(tokens)
    return result

config = get_configs("openai/VIT-B-32")
model = CLIP(**config)
model.load_state_dict(torch.load("logs/cliplim_4.19_fined.pth"))
model.eval()
# model, preprocess = model.load('logs/best_epoch_weights.pth', device = "cpu")

item_list = ["refrigerator","cabinet", "bed", "chair", "couch", "table", "door", "window",
             "bookshelf", "picture", "blinds", "shelves", "curtain", "dresser", "pillow", "mirror", "clothes",
             "ceiling", "books", "television", "paper", "towel", "shower", "box", "whiteboard", "night", "toilet",
             "sink", "lamp", "bathtub", "bag", "bar", "hallway", "keyboard", "fan", "sofa"]
item_list_test = ["refrigerator", "sofa", "bed", "chair", "door"]
#item_list_test = ["sofa", "sofa", "sofa"]
for item in item_list:
    item = "" + item

image_size = [224, 224]
device = "cpu"
transform = transforms.ToTensor()

picture = "img/target_image1.jpg"
image = preprocess(Image.open(picture), image_size)
image_tensor = torch.unsqueeze(transform(image), 0).to(device)

depth_picture = "img/target_image_depth1.jpg"
depth_image = preprocess(Image.open(depth_picture), image_size)
depth_image_tensor = torch.unsqueeze(transform(depth_image), 0).to(device)
#将原本是单通道的深度图扩张到3通道
depth_image_tensor = depth_image_tensor.expand(1,3,224,224)

with torch.no_grad():
    # image_features = model.encode_image(image)
    # text_features = model.encode_text(text)
    # depth_image_features = model.encode_depth_image(depth_image)

    logits_per_image, logits_per_text = model(image_tensor, item_list_test, depth_image_tensor)
    #probs = logits_per_image.numpy()
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()
    index = np.argmax(probs[0, :])

print("target_list is:", item_list_test)
print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]
max_indexes = np.argsort(probs[0])[-10:]
print("max_indexes is:", max_indexes)
for index in max_indexes:
    print(f"target is :{item_list_test[index]},target prob is :{probs[0][index]}")

#查看网络存在的键-值
# my_dict = torch.load('logs/best_epoch_weights.pth')
# for key in my_dict.keys():
#     print(key)
