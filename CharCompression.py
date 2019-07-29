s = str(raw_input())
t = ''
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        t = t + s[i]

print t