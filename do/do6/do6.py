###你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
import do.do4.do4
import os


def calc_dir_word_num(path):
    for file in os.listdir(path):
        file1 = os.path.join(path, file)
        Words = do.do4.do4.calc_word_num(file1)
        if Words == True:
            print("")
        else:
            print(file1, Words[0])



if __name__ == '__main__':
    print(calc_dir_word_num("test"))
