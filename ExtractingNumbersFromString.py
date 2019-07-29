s = str(raw_input())
t = ""
# Extracts Numbers from a String and displays a list
res = [int(i) for i in s.split() if i.isdigit()]

print("The numbers list is : " + str(res))
