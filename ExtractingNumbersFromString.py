s = str(raw_input())
t = ""
res = [int(i) for i in s.split() if i.isdigit()]

print("The numbers list is : " + str(res))
