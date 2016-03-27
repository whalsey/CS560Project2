import pickle
import sys

def intersect(list1, list2):
    ret = []
    for item in list1:
        if item in list2:
            ret.append(item)
    return ret

try:
    queryDict = pickle.load(open("queryDict.p", 'rb'))
except:
    import queryBuilder
    queryDict = pickle.load(open("queryDict.p", 'rb'))

key = "Doc1"


def writeList(list):
    base = ""
    for item in list:
        base += str(item) + ","
    print(base)


def readStdIn(file):
    for line in file:
        yield line.strip()

data = readStdIn(sys.stdin)
for line in data:
    line = line.strip()
    words = line.split(" ")
    listolists = []
    for word in words:
        word = word.lower()
        if word in queryDict[key]:
            listolists.append(queryDict[key][word])
    if len(listolists) < 2:
        if len(listolists) == 0:
            sys.stdout.write("The query you entered was not found")
        elif len(listolists) == 1:
            writeList(listolists[0])
    else:
        baseList = intersect(listolists[0], listolists[1])
        for i in range(2, len(listolists)):
            baseList = intersect(baseList, listolists[i])
        writeList(baseList)

