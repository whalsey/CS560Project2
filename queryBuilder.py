import pickle

infile = "finalOut.txt"
fin = open(infile, 'r')
lines = fin.readlines()

base = {}
for line in lines:
    line = line.strip()
    tag, word, elems = line.split(":")
    if tag not in base.keys():
        base[tag] = {}

    linenums = elems.split(",")
    templist = []
    for linenum in linenums:
        linenum.strip()
        try:
            templist.append(int(linenum))
        except ValueError:
            continue
    templist.sort()
    base[tag][word] = templist

pickle.dump(base, open("queryDict.p", 'wb'))
