#read doc, add line numbers to everything, figure out stop words (I suggest reading from a file)

fileName = 'pg100.txt'

lines = open(fileName).readlines()[175:]

test = "Have $1,000.00 for [fiddling] with (python)"
test = test.strip(".,:#$%^&*()[]?!\n").lower() + ' ' + str(index) + '\n'

wordCounts = {}
newLines = []
index = 176
for line in lines:
    if len(line.strip()) !=0:
        newLine = line.strip(".,:#$%^&*()[]?!\n").lower() + ' ' + str(index) + '\n'
        found = newLine.find("\' ")
        if found != -1:
            newLine = newLine[1:found] + newLine[found+1:-1]+'\n'
        found = newLine.find(" \'")
        if found != -1:
            newLine = newLine[1:found+1] + newLine[found+2:-1]+'\n'
        words = newLine.split(' ')
        for word in words:
            if word in wordCounts:
                wordCounts[word] +=1
            else:
                wordCounts[word] =1
        newLines.append(newLine)
    index += 1

newFile = open('pg100Editted.txt', 'w')
for line in newLines:
    newFile.write(line)

wordCountFile = open('wc.txt', 'w')

import operator

sorted_x = sorted(wordCounts.items(), key=operator.itemgetter(1),reverse=True)


for pairs in sorted_x:
    wordCountFile.write(pairs[0].strip() + ":" + str(pairs[1]) + '\n')
