# This funcion returns factoril of a number.
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


# It returns nth numner in Fibonacci series.
def fibonacci(n):
    if n == 1 or n == 2:
        return n-1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


n_1 = 10
fibo_number = fibonacci(n_1)
print(f"{n_1}th number in the fibonacci series is {fibo_number}.")




