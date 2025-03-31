def factorial(a):
    if a <= 1:
        an = 1
    else:
        an = factorial(a-1) * a

    return an

print(factorial(int(input())))