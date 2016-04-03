#!/usr/bin/python
import sys

reducerUseStdOut = False

class Reducer:
    '''Reduces'''
    @staticmethod
    def reduce(line):
        word, index = line.split("\t")
        tag, word = word.split(":")
        return tag, word, index

    @staticmethod
    def main(fin, fout = None):
        if fout is None:
            if reducerUseStdOut:
                fout = sys.stdout
            else:
                fout = open('finalOut.txt', 'w')
        current_word = None
        current_tag = None
        current_list = []
        for line in fin:
            line = line.rstrip()
            tag, word, linenum = Reducer.reduce(line)
            if current_tag is None:
                current_tag = tag
            if current_word is None:
                current_word = word
            if len(word) == 0:
                pass
            elif word == current_word:
                current_list.append(linenum)
            else:
                outline = tag + "|:" + current_word + "|:"
                for item in current_list:
                    outline += item + ", "
                outline = outline.rstrip(", ")
                fout.write(outline+"\n")

                current_word = word
                current_list = [linenum]

    if __name__ == "__main__":
        main(sys.stdin, sys.stdout)
