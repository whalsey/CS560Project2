#!/usr/bin/python
import sys
import os

class Mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    listOfFiles = []
    fout = sys.stdout
    fin = sys.stdin
    def __init__(self, foutname: str = None, dirname: str = None) -> None:
        if foutname is not None:
            self.fout = open(foutname, 'w')
        self.readDirectory(dirname)
        self.readStopWords()

    def readStopWords(self):
        if len(self.stopWords) == 0:
            file = "stopwords.txt"
            lines = open(file).readlines()
            for line in lines:
                self.stopWords.append(line.strip().strip())

    def processLine(self, line):
        line = line.strip()
        words = line.split(' ')
        try:
            index = int(words[-1])
        except ValueError:
            print("Please ensure all files in the directory are properly formatted (run preprocessing.py on each file).")
            exit()

        words.pop()#Pop the appended line number
        for word in words:
            if word not in self.stopWords:
                self.fout.write(word + "\t" + str(index)+'\n')


    def map(self, fileName):
        file = []
        try:
            file = open(fileName, 'r').readlines()
        except IOError:
            print("Directory")
            return

        for line in file:
            self.fout.write(fileName + ":")
            self.processLine(line)

    def readDirectory(self, dirname):
        self.listOfFiles = os.listdir(dirname)


    @staticmethod
    def main(foutname="mappedOut.txt", dirname="pg100Editted.txt"):
        m = Mapper(foutname, dirname)
        for file in m.listOfFiles:
            m.map(file)



if __name__ == "__main__":
    arg1 = None
    arg2 = "./processed/"
    if len(sys.argv) > 2:
        arg1 = sys.argv[2]
        arg2 = sys.argv[1]
    elif len(sys.argv) == 2:
        arg2 = sys.argv[1]
    Mapper.main(arg1, arg2)
