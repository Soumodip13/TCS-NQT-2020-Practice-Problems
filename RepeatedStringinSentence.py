from collections import Counter
s = str(raw_input())
res = s.split()
print Counter(res)
print type(Counter(res))
