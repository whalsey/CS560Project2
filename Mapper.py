#!/usr/bin/python
import sys
import os

class Mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    listOfFiles = []
    fout = sys.stdout
    fin = sys.stdin

    def __init__(self, foutname = None, dirname  = None): # -> None:
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

    def processLine(self, line, tag):
        line = line.strip()
        words = line.split(' ')
        try:
            index = int(words[-1])
        except ValueError:
            # print("Please ensure all files in the directory are properly formatted (run preprocessing.py on each file).")
            exit()

        words.pop()#Pop the appended line number
        for word in words:
            if word not in self.stopWords:
                self.fout.write(tag + "|:" + word + "\t" + str(index)+'\n')


    def map(self):
        for line in self.fin:
            filename = os.environ['map_input_file']
            self.processLine(line, filename)

    def readDirectory(self, dirname):
        if dirname is not None:
            self.directoryName = dirname
            baselist = os.listdir(dirname)
            for file in baselist:
                if(dirname.endswith("/") or dirname.endswith("\\")):
                    self.listOfFiles.append(dirname+file)
                else:
                    self.listOfFiles.append(dirname + "/" + file)

    @staticmethod
    def main(foutname=None, dirname="pg100Editted.txt"):
        m = Mapper(foutname, dirname)
        m.map()

if __name__ == "__main__":
    arg1 = None
    arg2 = None
    # if len(sys.argv) > 2:
    #     arg1 = sys.argv[2]
    #     arg2 = sys.argv[1]
    # elif len(sys.argv) == 2:
    #     arg2 = sys.argv[1]
    Mapper.main(arg1, arg2)
