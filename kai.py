def factorial(n):
    if n == 0:
        return 1  # The factorial of 0 is defined as 1.
    else:
        return n * factorial(n - 1)

# Input a number for which you want to calculate the factorial
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
