#!/bin/python3.10

from helper import getData

inputFile1 = "./dictionaries/dictionaryformathematicians1.zst"
inputFile2 = "./dictionaries/dictionaryformathematicians2.zst"
outputFile = "./answerDict.zst"
count = 1  # int(input("Number of times to append: "))

with open(inputFile1, 'rb') as file:
    inputFile1Data = file.read()
inputFile2Data = getData(inputFile2)

with open(outputFile, 'wb') as file:
    file.write(inputFile1Data)
    for _ in range(count):
        file.write(inputFile2Data)
