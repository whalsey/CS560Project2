import pickle

infile = "finalOut.txt"
fin = open(infile, 'r')
lines = fin.readlines()

key = "Doc1"
base = {key:{}}
for line in lines:
    line = line.strip()
    word, elems = line.split(":")
    linenums = elems.split(", ")
    templist = []
    for linenum in linenums:
        try:
            templist.append(int(linenum))
        except ValueError:
            pass
    templist.sort()
    base[key][word] = templist

pickle.dump(base, open("queryDict.p", 'wb'))