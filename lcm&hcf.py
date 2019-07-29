def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


lcm = 15*3//gcd(15, 3)
print lcm
