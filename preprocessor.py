##
#   preprocessor.py written by
#       Isaac Sherman   isherman@vols.utk.edu
#       William Halsey  whalsey@vols.utk.edu
#


#read doc, add line numbers to everything, figure out stop words (I suggest reading from a file)
import Mapper
from Reducer import Reducer
import operator
import sys


#r = Reducer()
#reduceFin = open('sortedOut.txt', 'r')
#r.main(reduceFin)
#print("Done reducing")

def realStrip(string, targets):
    targets = str(targets)
    for char in targets:
        string = string.replace(char, '')
    return string


USAGE = "python preprocessor fileName startingIndex\n filename is 'pg100.txt' by default, and startingIndex is 175"

fileName = 'pg100.txt'

if len(sys.argv) > 1:
    fileName = sys.argv[1]

startingIndex = 175
if len(sys.argv) > 2:
    try:
        startingIndex = int(sys.argv[2])
    except ValueError:
        print(USAGE)
        exit()

lines = open(fileName).readlines()[startingIndex:]

wordCounts = {}
newLines = []
index = startingIndex+1
for line in lines:
    if len(line.strip()) != 0:
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

outFile = fileName.strip(".txt") + "Editted.txt"
newFile = open('./processed/'+outFile, 'w')
newFile.writelines(newLines)

wordCountFile = open('wc.txt', 'w')


sorted_x = sorted(wordCounts.items(), key=operator.itemgetter(1),reverse=True)


for pairs in sorted_x:
    wordCountFile.write(pairs[0].strip() + ":" + str(pairs[1]) + '\n')

Mapper.Mapper.main("mappedOut.txt", "./processed/")  # Generates MappedOut.txt
mapped = open('mappedOut.txt', 'r').readlines()
mapped.sort()
sortedOut = open('sortedOut.txt', 'w')
sortedOut.writelines(mapped)
r = Reducer()
reduceFin = open('sortedOut.txt', 'r')
r.main(reduceFin)
