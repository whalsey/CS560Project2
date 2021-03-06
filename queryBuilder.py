##
#   queryBuilder.py written by
#       Isaac Sherman   isherman@vols.utk.edu
#       William Halsey  whalsey@vols.utk.edu
#
import sys
import pickle


infile = "finalOut.txt"

if len(sys.argv) > 1:
    infile = sys.argv[1]

fin = open(infile, 'r')
lines = fin.readlines()

base = {}
for line in lines:
    line = line.strip()
    tag, word, elems = line.split("|:")
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
