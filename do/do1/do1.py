"""
生成一定数量的激活码，并且保存进文本
"""
import random
import string

charlist = string.ascii_letters
numberlist = string.digits


def random_code(charlen, numlen):
    sl = []
    for i in range(charlen):
        sl.append(random.choice(charlist))
    for i in range(numlen):
        sl.append(random.choice(numberlist))
    random.shuffle(sl)
    return "".join(sl)


def random_codes(charlen, numlen, count):
    codel = []
    while count > 0:
        code = random_code(charlen, numlen)
        if code not in codel:
            codel.append(code)
            count -= 1
    return codel


def random_codes_file(charlen, numlen, count, out_file):
    codes = random_codes(charlen, numlen, count)
    with open(out_file, 'a+') as f:
        for c in codes:
            f.write(c + '\n')
        f.close()


if __name__ == '__main__':
    random_codes_file(5, 5, 10000, "codes.txt")
