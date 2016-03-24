#read doc, add line numbers to everything, figure out stop words (I suggest reading from a file)

fileName = 'pg100.txt'

lines = open(fileName).readlines()[175:]

newLines = []
index = 175
for line in lines:
    newLine = line.strip() + str(index) + '\n'
    index += 1
    newLines.append(newLine)

newFile = open('pg100Editted.txt', 'w')
for line in newLines:
    newFile.write(line)

