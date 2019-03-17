import urllib
import http.client
import json
import os
import subprocess
def getBestCaption(givenString):
    i = givenString.index('caption') + 11
    result = ""
    while(givenString[i] != '"'):
        result = result + givenString[i]
        i = i + 1
    return result

def assignResult(fnum, imgnum):
output = open('C:/Users/Kassym/Desktop/test_files/'+str(fnum)+"/output", "w")
output.write(str(imgnum))
close(output)
return str(imgnum)

print(assignResult(21, 100))

def getResults():
    for i in range(1, 26):
        input = open('C:/Users/Kassym/Desktop/test_files/'+str(fnum)+"/input", "r")
        caption_list = []
        for j in range(1, 7):
            caption_list.append(getCaption(i, j))                              
        print(caption_list)
        imgnum = compare(input.read(), caption_list)
        assignResult(fnum, imgnum)
getResults()
