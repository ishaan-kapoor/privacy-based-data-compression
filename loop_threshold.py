#!/bin/python3.10

from helper import factorize, factors2str, getData

referenceFile = "./dictionaries/email1.zst"
inputFile = "./dictionaries/email2.zst"
referenceData = getData(referenceFile)
inputData = getData(inputFile)
with open(referenceFile, 'rb') as file: refData_withMeta = file.read()
factors = factorize(inputData, referenceData)

for threshold in (*range(11), 15, 20, float('inf')):
    shortlisted_factors = filter(lambda x: x[1] <= threshold, factors)
    mergedData = factors2str(referenceData, shortlisted_factors)

    outputFile = f"./output_dictionaries/meta_threshold{threshold}.zst"
    with open(outputFile, 'wb') as file:
        file.write(refData_withMeta)
        file.write(mergedData)

    outputFile = f"./output_dictionaries/threshold{threshold}.zst"
    with open(outputFile, 'wb') as file:
        file.write(referenceData)
        file.write(mergedData)
