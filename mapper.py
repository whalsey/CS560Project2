import sys

import reducer
class Mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    r = reducer.reducer()
    fout = sys.stdout
    fin = sys.stdin
    def __init__(self, foutname = None, finname = None):
        if(foutname != None):
            self.fout = open(foutname, 'w')
        if finname != None:
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

    def main(self, foutname="mappedOut.txt", finname="pg100Editted.txt"):
        self.__init__(foutname, finname);
        for line in self.fin:
            self.map(line)

    if __name__ == "__main__":
        main()
