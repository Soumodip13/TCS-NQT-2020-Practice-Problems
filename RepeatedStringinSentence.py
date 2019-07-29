from collections import Counter
s = str(raw_input())
res = s.split()
# counts the number of times a string is repeated in a sentence
print Counter(res)
print type(Counter(res))
