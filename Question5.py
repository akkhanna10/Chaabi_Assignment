# ================== PROBLEM STATEMENT ===================
"""
Given 2 lists in input. Write a program to return the elements, which
are common to both lists (set intersection) and those which are not
common (set symmetric difference) between the lists.
"""

# ================== SOLUTION ===================


def commonAndDifference(mainstream, must_watch):
    common_elements = list(set(mainstream) & set(must_watch))
    symmetric_difference = list(set(mainstream) ^ set(must_watch))
    return common_elements, symmetric_difference


# Driver Code


mainstream = [
    "One Punch Man",
    "Attack On Titan",
    "One Piece",
    "Sword Art Online",
    "Bleach",
    "Dragon Ball Z",
    "One Piece",
]
must_watch = [
    "Full Metal Alchemist",
    "Code Geass",
    "Death Note",
    "Stein's Gate",
    "The Devil is a Part Timer!",
    "One Piece",
    "Attack On Titan",
]

common, symmetric = commonAndDifference(mainstream, must_watch)
print("[" + ", ".join(f'"{elem}"' for elem in common) + "],")
print("[" + ", ".join(f'"{elem}"' for elem in symmetric) + "]")
