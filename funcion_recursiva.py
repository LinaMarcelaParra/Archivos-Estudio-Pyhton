def factorial(num):
    if num> 1:
            num	*= factorial(num - 1)
    return num
print(factorial(5))
