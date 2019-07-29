def reverse(s):
    return s[::-1]

# Checks a string is Palindrome or not
s = str(raw_input())
t = reverse(s)
if s == t:
    print 'Palindrome found'
else:
    print 'Not Palindrome'
