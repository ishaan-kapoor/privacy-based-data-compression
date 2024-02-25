#!/bin/python3.10

from helper import getData

inputFile = "./dictionaries/dictionaryformathematicians2.zst"
outputFile = "./answerDict.zst"
inputFileData = getData(inputFile)
with open(outputFile, 'wb') as file: file.write(inputFileData)
