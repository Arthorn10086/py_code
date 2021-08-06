##任一个英文的纯文本文件，统计其中的单词出现的个数。
import os, re
import collections

def calc_word_num(file):
    if os.path.isfile(file):
        pattern = r'''[A-Za-z]+|\$?\d+%?$'''
        with open(file, "r") as f:
            content = f.read().lower()
            r = re.findall(pattern, content)
            c = collections.Counter(r)
            return c.most_common()
    else:
        print("not file", file)
        return True




if __name__ == '__main__':
    print(calc_word_num("test.txt"))
