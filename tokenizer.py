import os
import re
import sys

#this should run linear time compared to N where N is the number of words in the file. 
#the double for loop is just going through every word once. O(N)
def tokenize(TextFilePath):
    #check if file exists
    tokenList = []
    if os.path.exists(TextFilePath):
        with open(TextFilePath, encoding="utf-8") as f:
            while True:
                try:
                    for l in f:
                        words = re.findall(r"\w+\'?\w*", l.lower())
                        for word in words:
                            tokenList.append(word)
                    break
                except:
                    pass
    return tokenList
    
#should take O(NlogN) time, it should only need to loop through all the words once to count them all. 
# sorted takes NlogN time so the time complexity boils down to NLogN + N time
def computeWordFrequencies(tokenList):
    tokenMap = {}
    if type(tokenList) == list:
        for word in tokenList:
            tokenMap[word] = tokenMap.get(word, 0) + 1
    return dict(sorted(tokenMap.items(), key=lambda x:x[1], reverse=True))

#simple O(N) loop through every item in the dictionary oncee. 
def printD(map):
    if type(map) == dict:
        for key, value in map.items():
            print(f"{key} - {value}")

#in total around n^3 time maybe like (nlogn)^3 not completely sure
if __name__ == '__main__':
    file = sys.argv[1]
    printD(computeWordFrequencies(tokenize(file)))