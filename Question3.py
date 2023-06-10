# ======================PROBLEM========================
'''
Given a list of dicts, write a program to sort the list according
to a key given in input.

'''

# =====================SOLUTION=========================


def sortDicts(list_of_dicts, key):
    # Here sorted fuction is used with list_of_dicts as iterable to
    # sort and key as lambda function to sort on the basis of key
    return sorted(list_of_dicts, key=lambda x: x.get(key))


# Driver Code
list_of_dicts = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sortedDicts = sortDicts(list_of_dicts, "fruit")
print(sortedDicts)

sortedDicts = sortDicts(list_of_dicts, "color")
print(sortedDicts)
