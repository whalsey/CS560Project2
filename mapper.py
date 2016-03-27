#!/usr/bin/python
import sys

class Mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    fout = sys.stdout
    fin = sys.stdin
    def __init__(self, foutname: str = None, finname: str = None) -> None:
        if foutname is not None:
            self.fout = open(foutname, 'w')
        if finname is not None:
            self.fin = open(finname, 'r')
        self.readStopWords()
    def readStopWords(self):
        if len(self.stopWords) == 0:
            file = "stopwords.txt"
            lines = open(file).readlines()
            for line in lines:
                self.stopWords.append(line.strip().strip())

    def map(self, line):
        line = line.strip()
        words = line.split(' ')
        index = int(words[-1])
        words.pop()#Pop the appended line number
        for word in words:
            if word not in self.stopWords:
                self.fout.write(word + "\t" + str(index)+'\n')

    @staticmethod
    def main(foutname="mappedOut.txt", finname="pg100Editted.txt"):
        m = Mapper()
        m.__init__(foutname, finname)
        for line in m.fin:
            m.map(line)

if __name__ == "__main__":
    Mapper.main(None, None)
