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

def writeList(list):
    base = ""
    if len(list) == 0:
        base = "No terms found"
    else:
        for item in list:
            base += str(item) + ","
    base = base.strip(",")
    print(base)


def readStdIn(file):
    for line in file:
        yield line.strip()


def doQuery(line):
    line = line.strip()
    words = line.split(" ")
    listolists = []
    for key in queryDict.keys():
        for word in words:
            word = word.lower()
            if word in queryDict[key]:
                temtem = []
                for linenum in queryDict[key][word]:
                    temtem.append(key + ":" + str(linenum))
                listolists.append(temtem)
    if len(listolists) < 2:
        if len(listolists) == 0:
            print("The query you entered was not found.")
        elif len(listolists) == 1:
            writeList(listolists[0])
    else:
        baseList = intersect(listolists[0], listolists[1])
        for i in range(2, len(listolists)):
            baseList = intersect(baseList, listolists[i])
        writeList(baseList)


while (1):
    line = input("Enter query terms, or q to exit:")
    if line == "q":
        break
    doQuery(line)
