def factorial(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return i*factorial(i-1)


n = int(input("Enter n"))
p = int(input("Enter p"))
npr = factorial(n)/factorial(n-p)
print npr
