test_string = str(raw_input())

print("The original string : " + test_string)
res = ''.join(filter(lambda i: i.isdigit(), test_string))
print("The digits string is : " + str(res))