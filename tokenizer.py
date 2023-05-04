import os
import re
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#code gotten from "https://www.geeksforgeeks.org/removing-stop-words-nltk-python/"


def tokenize(Text):
    #check if file exists
    tokenList = []
    for t in word_tokenize(Text):
        if t.lower() not in stopwords:
            tokenList.append(t)
    return tokenList
    
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