s = str(raw_input())
count = 0
for i in range(len(s)):
    if s[i] == '.':
        count += 1

res = s.split()
print len(s)
print len(res)
print count
print "Avg words per sentence", len(s)/count
