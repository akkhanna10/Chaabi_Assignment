# ===================PROBLEM=======================
"""
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days
away from each other, else returns False.

"""
# ===================SOLUTION======================


from datetime import datetime


def datesDifference(from_date, to_date, difference):
    # Converting string to date time object
    from_date = datetime.strptime(from_date, "%y-%m-%d")
    to_date = datetime.strptime(to_date, "%y-%m-%d")

    # Calculating the diffrence between from_date and to_date
    date_difference = abs((to_date - from_date).days)

    # Checking if the date_difference is less than difference
    if date_difference < difference:
        # If YES return True
        return True
    else:
        # Else False
        return False


# Driver code
# Test Case 1
res = datesDifference("21-01-01", "21-01-10", 10)
print(res)
# Test Case 2
res = datesDifference("21-01-01", "21-01-15", 10)
print(res)
