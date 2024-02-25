#!/bin/python3.10

from helper import getData

inputFile1 = "./dictionaries/email1.zst"
inputFile2 = "./dictionaries/email2.zst"
count = 6

with open(inputFile1, 'rb') as file: inputFile1Data_withMeta = file.read()
inputFile1Data = getData(inputFile1)
inputFile2Data = getData(inputFile2)

append_data = b''
for i in range(1, count+1):
    append_data += inputFile2Data

    outputFile = f"./output_dictionaries/meta_append{i}.zst"
    with open(outputFile, 'wb') as file:
        file.write(inputFile1Data_withMeta)
        file.write(append_data)

    outputFile = f"./output_dictionaries/append{i}.zst"
    with open(outputFile, 'wb') as file:
        file.write(inputFile1Data)
        file.write(append_data)
