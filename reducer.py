#!/usr/bin/python
import sys


class Reducer:
    '''Reduces'''

    @staticmethod
    def reduce(line):
        word, index = line.split("\t")
        return word, index

    @staticmethod
    def main(fin):
        r = Reducer()
        #fout = open('finalOut.txt', 'w')
        current_word = None
        current_list = []
        for line in fin:
            line = line.rstrip()
            word, linenum = r.reduce(line)

            if current_word is None:
                current_word = word
            if len(word) == 0:
                pass
            elif word == current_word:
                current_list.append(linenum)
            else:
                outline = current_word + ":"
                for item in current_list:
                    outline += item + ", "
                print(outline)
                current_word = word
                current_list = [linenum]

    if __name__ == "__main__":
        main(sys.stdin)
