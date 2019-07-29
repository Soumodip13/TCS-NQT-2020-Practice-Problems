s = str(raw_input())
res = s.split()
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
words = []
count = 0
# Counts and shows the number of words in a sentence that starts with a vowel
for i in range(len(res)):
    if res[i][0] in vowels:
        count += 1
        words.append(res[i])

print words
print count
print list(set(res)-set(words))