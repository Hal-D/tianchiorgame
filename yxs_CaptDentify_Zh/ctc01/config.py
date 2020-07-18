import numpy as np
import albumentations as alb
import cv2

pre_weight = "output/bm_largechannel_csse.epoch=277-val_acc=0.57521.ckpt"
prefix = "bm_largechannel_csse"  # 权重保存前缀

key_words = "-" + open("kw_zh.txt",encoding='UTF-8').readline().strip()

num_classes = len(key_words)
minL = 4
maxL = 8

n_input_length = 24
W,H = 192,64 # 自定义模型参数

batch_size = 128
lr = 1e-4
epochs = 1000
weight_decay = 1e-3

transforms_val = alb.Compose([
    alb.Resize(height=H, width=W, p=1),
    alb.Normalize(),
])
transforms_train = alb.Compose([


    alb.Resize(height=H, width=W, p=1),

    alb.ShiftScaleRotate(rotate_limit=5,shift_limit=0.0625,scale_limit=0.1,p=0.2,border_mode=cv2.BORDER_REPLICATE),
    alb.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=10, val_shift_limit=10,p=0.2),
    alb.RGBShift(r_shift_limit=10,g_shift_limit=10,b_shift_limit=10,p=0.2),
    alb.ChannelShuffle(p=0.2),
    alb.InvertImg(p=0.2),
    alb.OneOf([
        # 畸变相关操作
        alb.OpticalDistortion(p=0.3),
        alb.GridDistortion(p=.1),
    ], p=0.2),

    alb.Normalize(),
])
