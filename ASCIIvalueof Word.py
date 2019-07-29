s = str(raw_input())
res = 0
for i in range(len(s)):
    print ord(str(s[i]))
    res = res + ord(str(s[i]))

print res