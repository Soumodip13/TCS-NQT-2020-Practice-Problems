number = int(input())


def factorial(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return i*factorial(i-1)


print factorial(number)