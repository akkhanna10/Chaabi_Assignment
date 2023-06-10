# =================PROBLEM================
"""
Given a list and 2 indices as input, return the sub-list enclosed within
these 2 indices. It should contain every second element.

"""
# ===============SOLUTION================


def subList(list, start, end):
    # slicing the list from start to end with every step
    subList = list[start:end+1:2]
    return subList


# Driver code
list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start = 2
end = 9
result = subList(list, start, end)
print(result)
