def reverse(s):
    return s[::-1]


number = int(input())
s = str(number)
t = reverse(s)
if s == t:
    print 'Number is a Palindrome'
else:
    print 'Number is not a Palindrome'