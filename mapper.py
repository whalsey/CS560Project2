class mapper:
    '''Takes a number of lines (with the line number appended after a space) and returns a list of words and indices'''
    stopWords = []
    def __init__(self):
        self.readStopWords()
    def readStopWords(self):
        if len(self.stopWords) == 0:
            file = "stopwords.txt"
            lines = open(file).readlines()
            for line in lines:
                self.stopWords.append(line.strip().strip())

    def map(self, lines):
        ret = []
        self.readStopWords()
        for line in lines:
            line = line.strip()
            words = line.split(' ')
            index = int(words[-1])
            words.pop()#Pop the appended line number
            for word in words:
                if word not in self.stopWords:
                    pair = {word: index}
                    ret.append(pair)
        return ret


