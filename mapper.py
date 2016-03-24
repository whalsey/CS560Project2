class mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    def readStopWords(self):
        file = "stopwords.txt"
        lines = open(file).readlines()
        for line in lines:
            self.stopWords.append(line.strip())
    def map(self, lines):
        ret = []
        readStopWords()
        for line in lines:
            line = line.strip()
            words = line.split(' ')
            index = int(words[-1])
            words.pop()#Pop the appended line number
            for word in words:
                pair = {word: index}
                ret.append(pair)


