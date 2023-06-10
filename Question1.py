# =====================PROBLEM============================
'''
Q1. Get your basics right - Implement selection sort algorithm in python.
The function accepts a list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]

'''

# =====================SOLUTION============================


# Python program for implementation of Selection
# Sort
def selectionSort(list):
    # Iterating the given array
    for i in range(len(list)):
        # Finding the minimum element in each iteration.
        minimum_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minimum_index]:
                minimum_index = j

        # Swap the minimum element with the first element of the unsorted part
        list[i], list[minimum_index] = list[minimum_index], list[i]
    return list


# Driver code
if __name__ == "__main__":
    # Test the selectionSort function
    list = [5, 416, 54, 21, 6135, 15, 741]
    res = selectionSort(list)
    print(res)
