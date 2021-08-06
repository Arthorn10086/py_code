"""
在图片的右下角加上文本信息
"""
from PIL import Image, ImageDraw, ImageFont


def add_text(img, str):
    # 打开图片
    im = Image.open(img).convert('RGB')
    # 加载一个TrueType或者OpenType字体文件，并且创建一个字体对象
    tfont = ImageFont.truetype('Candarab.ttf', 30)
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(im)
    # 拿到图像的宽高
    width, height = im.size
    print(width, height)
    # 在给定的位置绘制一个字符创。(xy,text,fill,front)  xy偏移坐标  初始左上角的位置 |  fill字体颜色 | font 字体类型 ImageFont
    draw.text((width - 160, height - 160), str, fill='yellow', font=tfont)
    # 保存
    im.save('do0_1.jpg')


if __name__ == '__main__':
    add_text('do0.jpg', 'a')
