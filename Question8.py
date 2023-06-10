# ====================PROBLEM=======================
'''
Looking at the below code, write down the final values of A0, A1, ...An
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

'''
# ====================SOLUTION======================


# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# Final Value : {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Explanation : A0 is assigned a dictionary with ('a','b','c','d','e') as key
# (1,2,3,4,5) as value using zip method.


# A1 = range(10)
# Final Value : range(0, 10)
# Explanation : A1 is assigned a range from 0 to 9.


# A2 = sorted([i for i in A1 if i in A0])
# Final Value : []
# Explanation : It is checking if 0-9 is key in A0. Since,
# A0 has letters as key. So, it is empty.


# A3 = sorted([A0[s] for s in A0])
# Final Value : [1, 2, 3, 4, 5]
# Explanation : Retrieving the values of keys in dict A0.


# A4 = [i for i in A1 if i in A3]
# Final Value : [1, 2, 3, 4, 5]
# Explanation: Filtering the value in A3.


# A5 = {i:i*i for i in A1}
# Final Value : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36,
# 7: 49, 8: 64, 9: 81}
# Explanation : Assigning A5 with with 0 to 9 as keys and square of
# key as value.


# A6 = [[i,i*i] for i in A1]
# Final Value : [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16],
# [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# Exaplanation : A6 is assigned a list of pairs where first element
# is from A1 and second element is square of the element.


# A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# Final Value : syntax error if we do not import reduce from functools
# and if we import it , then the value will be 21 as it adding
# subsequent elements.


# A8 = map(lambda x: x*2, [1,2,3,4])
# Final Value : [2, 4, 6, 8]
# Explanation : A8 is a map that modifies elements of list [1,2,3,4]


# A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])
# Final Value : ['want', 'learn', 'python']
# Explanation : A9 filters out the strings that has length greater
# than 3.
