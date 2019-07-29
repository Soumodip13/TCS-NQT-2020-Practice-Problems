s = str(raw_input())
a = list(s)
# Changing the first character into 'A'
a[0] = 'A'
b = ""
for i in range(len(a)):
    b = b + a[i]

print b
# Changing the last character into 'A'
s1 = str(raw_input())
s12 = list(s1)
s12[-1] = 'A'
c = ""
for i in range(len(s1)):
    c = c + s12[i]

print c
