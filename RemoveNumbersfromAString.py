s = str(raw_input())
res = ''.join(filter(lambda x: not x.isdigit(), s))
print res