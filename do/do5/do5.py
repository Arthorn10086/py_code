##你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
from PIL import Image
import os


def change_image_size(img, max_x, max_y):
    im = Image.open(img)
    width, height = im.size
    w1, h1 = calc_resolution(width, height, max_x, max_y)
    print(w1, h1)
    im1 = im.resize((w1, h1), Image.ANTIALIAS)
    im1.save(img)


def change_image_size_by_folder(folder, x, y):
    for root, dirs, files in os.walk(folder):
        for f in files:
            change_image_size(os.path.join(root, f), x, y)


def calc_resolution(x, y, mx, my):
    if mx >= x:
        pass
    else:
        x = mx
        y = y * mx // x
    if my >= y:
        pass
    else:
        x = x * my // y
        y = my
    return x, y


change_image_size_by_folder("E:\py\images", 1136, 640)
