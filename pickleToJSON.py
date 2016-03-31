import pickle
import json

print("Loading pickled dictionary")
dictionary = pickle.load(open("queryDict.p", 'rb'))
print("Making JSON of pickle")
jsonOut = json.dump(dictionary, open("queryDict.json", 'w'))

print("Finished dump, loading")
testDict = json.load(open("queryDict.json"))

print("Testing")
failed = False
for tag in testDict.keys():
    if failed:
        break
    if tag not in dictionary.keys():
        failed = True
        break
    for word in testDict[tag].keys():
        if failed:
            break
        testList = testDict[tag][word]
        originalList = dictionary[tag][word]
        for item in testList:
            if item not in originalList:
                failed = True

if not failed:
    print("Test Passed")
else:
    print("Test Failed")

