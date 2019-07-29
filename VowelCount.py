s = str(raw_input())
t = ['a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'U', 'u']
count = 0
for i in range(len(s)):
            if s[i] in t:
                count = count + 1

print len(s)
print(count)
print(len(s) - count)