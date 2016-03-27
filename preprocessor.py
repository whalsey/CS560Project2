#read doc, add line numbers to everything, figure out stop words (I suggest reading from a file)

from Reducer import Reducer

r = Reducer()
reduceFin= open('sortedOut.txt', 'r')
r.main(reduceFin)

print("Done reducing")

def realStrip(string, targets):
    targets = str(targets)
    for char in targets:
        string = string.replace(char, '')
    return string


fileName = 'pg100.txt'

lines = open(fileName).readlines()[175:]

wordCounts = {}
newLines = []
index = 176
for line in lines:
    if len(line.strip()) !=0:
        newLine = realStrip(line, '.,:#$%^&*();<>[]?!\r\n"').lower() + ' ' + str(index) + '\n'
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

# m = mapper.Mapper()
# m.main()#Generates MappedOut.txt
# mapped = open('mappedOut.txt', 'r').readlines()
# mapped.sort()
# sortedOut = open('sortedOut.txt', 'w')
# sortedOut.writelines(mapped)
# r = reducer()
# reduceFin= open('sortedOut.txt', 'r')
# r.main(reduceFin)
#
#
