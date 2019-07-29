def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)


if __name__ == "__main__":
    num = int(input())
    s = fact(num)
    t = str(s)
    print len(t)
