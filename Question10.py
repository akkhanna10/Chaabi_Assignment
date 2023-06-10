# ====================PROBLEM=======================
'''
Of date and days
Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'

'''
# =====================SOLUTION=======================


from datetime import datetime, timedelta


def daysSubstraction(date, n):
    # Converting date string to datetime object.
    date_object = datetime.strptime(date, '%y-%m-%d')

    # Subtracting n days from the date.
    new_date = date_object - timedelta(days=n)

    # Format the new date as a string in the desired format
    new_date_string = new_date.strftime('%y-%m-%d')

    return new_date_string


# Driver Code
# Test Case 1
result = daysSubstraction('16-12-10', 11)
print(result)
