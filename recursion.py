def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return 0
    else: 
        return n * factorial(n-1)

n = 5
fact = factorial(n)
print(f"Factorial of {n} is {fact}.")