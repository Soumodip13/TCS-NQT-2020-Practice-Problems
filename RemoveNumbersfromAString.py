s = str(raw_input())
# Shows the string except numbers
res = ''.join(filter(lambda x: not x.isdigit(), s))
print res