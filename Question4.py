# ====================PROBLEM=====================
'''
Given a dictionary, switch position of key and values in the dict, i.e.,
value becomes the key and key becomes value. The function's body
shouldn't have more than one statement.

'''

# ====================SOLUTION=====================


def swapDict(dictionary):
    return {value: key for key, value in dictionary.items()}


# Driver Code
dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

res = swapDict(dictionary)
print(res)
