def reverse(s):
    return s[::-1]


s = str(raw_input())
t = reverse(s)
if s == t:
    print 'Palindrome found'
else:
    print 'Not Palindrome'
