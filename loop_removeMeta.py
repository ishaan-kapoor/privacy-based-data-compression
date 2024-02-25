#!/bin/python3.10
from helper import getData
# for i in range(1, 7):
#     file = f"./outputs/appendDict{i}.zst"
for threshold in (*range(11), 15, 20, float('inf')):
    file = f"./outputs/threshold{threshold}_withMeta.zst"
    data = getData(file)
    with open(file, 'wb') as file: file.write(data)
