s = str(raw_input())
count = 0
# Counts the number of sentences in a paragraph
for i in range(len(s)):
    if s[i] == '.':
        count += 1

print count
