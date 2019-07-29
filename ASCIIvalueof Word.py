s = str(raw_input())
res = 0
for i in range(len(s)):
    # Shows the ASCII value of a Character
    print ord(str(s[i]))
    # Adds the ASCII values
    res = res + ord(str(s[i]))

print res