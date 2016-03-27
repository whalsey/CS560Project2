import pickle

infile = "finalOut.txt"
fin = open(infile, 'r')
lines = fin.readlines()

key = "Doc1"
base = {key:{}}
for line in lines:
    line = line.strip()
    word, elems = line.split(":")
    if word == "yorick":
        pass
    linenums = elems.split(",")
    templist = []
    for linenum in linenums:
        linenum.strip()
        try:
            templist.append(int(linenum))
        except ValueError:
            continue
    templist.sort()
    base[key][word] = templist

pickle.dump(base, open("queryDict.p", 'wb'))
