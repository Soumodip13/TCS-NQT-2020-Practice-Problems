s = str(raw_input())
count = 0
for i in range(len(s)):
    if s[i] == '.':
        count += 1

print count
