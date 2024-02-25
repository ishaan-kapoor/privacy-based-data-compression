#!/bin/python3.10

from helper import factorize, factors2str, getData

referenceFile = "./dictionaries/archive4a.zst"
inputFile = "./dictionaries/archive4b.zst"
outputFile = "./answerDict.zst"
THRESHOLD = int(input("Threshold: "))
DEBUG = False

referenceData = getData(referenceFile)
inputData = getData(inputFile)
 
factors = factorize(inputData, referenceData)
shortlisted_factors = filter(lambda x: x[1] <= THRESHOLD, factors)
if DEBUG: print(factors)
if DEBUG: print(shortlisted_factors)

mergedData = factors2str(referenceData, shortlisted_factors)

with open(referenceFile, 'rb') as file:
    refFileData = file.read()
with open(outputFile, 'wb') as file:
    file.write(refFileData)
    file.write(mergedData)
