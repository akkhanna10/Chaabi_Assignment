# ========================PROBLEM==========================
"""
Find output of following:
def f(x,list=[]):
for i in range(x):
list.append(i*i)
print(list)
f(2)
f(3,[3,2,1])
f(3)

"""
# ========================SOLUTION===========================


# Code
def f(x, list=[]):  # Since l is ambigous, I am changing it to list.
    for i in range(x):
        list.append(i * i)
    print(list)


f(2)
f(3, [3, 2, 1])
f(3)


# OUTPUT
# f(2) will give [0, 1]
"""
Explanation: Since f(2) is called with x = 2 and list = [],
the for loop will iterate over 0 to 1 and appending
square of i in each iteration to the list. So, list becomes [0, 1].

"""
# f(3, [3, 2, 1]) will give [3, 2, 1, 0, 1, 4]
"""
Explanation: Since f(3, [3, 2, 1]) is called with x = 3 and
list = [3, 2, 1], the for loop will iterate over 0 to 2 and appending
square of i in each iteration to the list. So, list becomes
[3, 2, 1, 0, 1, 4].

"""

# f(3) will give [0, 1, 0, 1, 4]
"""
Explanation: Since f(3) is called with x = 3 and with list = [0, 1]
as list is mutable so the previously appended values are still there.
And after iterating over 0 to 2 and adding square of i in each iteration.
Hence, list becomes [0, 1, 0, 1, 4].

"""
