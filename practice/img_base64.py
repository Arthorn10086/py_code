import sys
import base64


def ImgToBase64(argv: list):
    inputfile = argv[2]
    outfile = argv[3]
    ifile = open(inputfile, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(ifile.read())  # 读取文件内容，转换为base64编码
    ifile.close()
    ofile = open(outfile, 'wb')
    ofile.write(ls_f)
    ofile.close()


def Base64ToImg(argv: list):
    inputfile = argv[2]
    outfile = argv[3]
    ifile = open(inputfile, 'rb')
    imgdata = base64.b64decode(ifile.read())
    ifile.close()
    ofile = open(outfile, 'wb')
    ofile.write(imgdata)
    ofile.close()
def Help():
    print('Usage:')
    print('    img_base64.py <enc|dec> <InFilePath> <OutFilePath>')
    print('')
    print('        <enc|dec>                "dec" img to base64, "enc" base64 to img.')
    print('')
    print('        <InFilePath>                   输入文件路径')
    print('')
    print('        <OutFilePath>                  输出文件路径')
    print('')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == 'enc':
            ImgToBase64(sys.argv)
        elif sys.argv[1] == 'dec':
            Base64ToImg(sys.argv)
        else:
            Help()
    else:
        Help()
