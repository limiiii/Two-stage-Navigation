#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-
import os
import numpy as np
import torch
import torch.distributed as dist

from nets.clip import CLIP
from utils.utils import get_configs
from copy import deepcopy


if __name__ == "__main__":
    Cuda                = True
    distributed         = False
    fp16                = False
    model_path1          = "logs/ViT-B-32-OpenAI.pth"
    model_path2          = "logs/cliplim_4.24.pth"
    phi                 = "openai/VIT-B-32"
    batch_size      = 64
    Init_Epoch      = 0
    Epoch           = 20
    Init_lr             = 1e-4
    Min_lr              = Init_lr * 0.01
    optimizer_type      = "adamw"
    momentum            = 0.9
    weight_decay        = 1e-2
    lr_decay_type       = 'cos'
    save_period         = 1
    save_dir            = 'logs'
    eval_flag           = True
    eval_period         = 1
    num_workers         = 1

    datasets_path               = "datasets/"
    datasets_train_json_path    = "datasets/train.json"
    datasets_val_json_path      = "datasets/val.json"
    datasets_random             = True

    ngpus_per_node  = torch.cuda.device_count()
    if distributed:
        dist.init_process_group(backend="nccl")
        local_rank  = int(os.environ["LOCAL_RANK"])
        rank        = int(os.environ["RANK"])
        device      = torch.device("cuda", local_rank)
        if local_rank == 0:
            print(f"[{os.getpid()}] (rank = {rank}, local_rank = {local_rank}) training...")
            print("Gpu Device Count : ", ngpus_per_node)
    else:
        device          = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        local_rank      = 0
        rank            = 0

    config  = get_configs(phi)
    model   = CLIP(**config)
    if model_path1 != '':
        if local_rank == 0:
            print('Load weights {}.'.format(model_path2))
        #------------------------------------------------------#
        #   根据预训练权重的Key和模型的Key进行加载
        #------------------------------------------------------#
            
        model_dict2      = model.state_dict()
        pretrained_dict = torch.load(model_path2, map_location = device)
        load_key, no_load_key, temp_dict = [], [], {}
        for k, v in pretrained_dict.items():
            if k in model_dict2.keys() and np.shape(model_dict2[k]) == np.shape(v):
                temp_dict[k] = v
                load_key.append(k)
            else:
                no_load_key.append(k)
        model_dict2.update(temp_dict)
        #改采用不完全匹配的方法加载参数
        model.load_state_dict(model_dict2, strict = False)
        
        print('Load weights {}.'.format(model_path1))
        model.load_state_dict(torch.load(model_path1, map_location = device), strict = False)
        #model.load_state_dict(model_dict)
        #------------------------------------------------------#
        #   显示没有匹配上的Key
        #------------------------------------------------------#
        if local_rank == 0:
            print("\nSuccessful Load Key:", str(load_key)[:500], "……\nSuccessful Load Key Num:", len(load_key))
            print("\nFail To Load Key:", str(no_load_key)[:500], "……\nFail To Load Key num:", len(no_load_key))
            print("\n\033[1;33;44m温馨提示，head部分没有载入是正常现象，Backbone部分没有载入是错误的。\033[0m")
    torch.save(deepcopy(model).half().state_dict(), os.path.join(save_dir, "cliplim_4.24_fined.pth"))
    
