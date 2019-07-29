a = input()
b = input()
c = bin(a).replace("0b", "")
d = bin(b).replace("0b", "")
z = (int(c) + int(d)) % 2
print c
print d
print z