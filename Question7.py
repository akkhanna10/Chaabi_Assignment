# =================PROBLEM=================
'''
Calculate the factorial of a number using lambda function.
'''
# ================SOLUTION=================


def factorialCalculator(n):
    factorial = (lambda func: lambda x: func(func, x))(
        lambda func, x: 1 if x == 0 else x * func(func, x - 1)
    )
    return factorial(n)


# Driver code
number = int(input().split()[0])
result = factorialCalculator(number)
print(f"The factorial of {number} is {result}")
