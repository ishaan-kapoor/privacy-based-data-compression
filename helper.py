#!/bin/python3.10
DEBUG = True if __name__ == "__main__" else False

def getData(dictFile):
    with open(dictFile, 'rb') as file:
        data = file.read() # reading f1 contents

    substring_to_find = bytes.fromhex("0000 0004 0000 0008 0000 00")
    index = data.find(substring_to_find)
    
    if(index == -1):
        substring_to_find = bytes.fromhex("00 0000 0400 0000 0800 0000")
        index = data.find(substring_to_find)
    if (index == -1):
        print("error")
        if DEBUG: print("Data not found in the input string.")
        exit()

    data_after_substring = b""
    if DEBUG: print(f"index: {index}\n")
    data_after_substring = data[index + len(substring_to_find):]
    return data_after_substring
    # metaData = S[:index + len(substring_to_find)]
    # print(type(metaData))
    # print("---------------metadata begin-----------------")
    # print(metaData) 
    # print("---------------metadata end  -----------------")

def factorize(inputData, referenceData):
    factors = []
    i = 0

    while i < len(inputData):
        factor_position = -1
        candidate_factor = inputData[i]

        if candidate_factor in referenceData:
            factor_position = referenceData.index(candidate_factor)
            length = 1
            # Check if the match can be extended
            for j in range(i + 1, len(inputData)):
                extended_factor = inputData[i:j + 1]
                if extended_factor in referenceData:
                    length += 1
                    factor_position = referenceData.index(extended_factor)
                else: break
            factors.append((factor_position, length))
            i += length
        else:
            factors.append((inputData[i], 0))
            i += 1

    return factors


# add to reference dictionary where the length is less than threshold
def factors2str(referenceData, factors):
    concatenated_bytes = b""
    for factor in factors:
        if factor[1] == 0:
            concatenated_bytes += chr(factor[0]).encode()
        else:
            start_index = factor[0]
            end_index = factor[0] + factor[1]
            concatenated_bytes += referenceData[start_index:end_index]
    return concatenated_bytes

if __name__ == "__main__":
    factors = [
        (0,9),
        ('d',0),
        ('m',0),
        (0,1),
        ('n',0),
        (12,1),
        (3,1),
        ('n',0),
    ]
    print(factors2str("i love basketball", factors))
