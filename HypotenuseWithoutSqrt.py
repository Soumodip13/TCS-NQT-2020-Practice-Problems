a = float(input())
b = float(input())
i = 0.0
# Implementation of Hypotenuse without math.sqrt
while i*i < (a*a + b*b):
         i = i + 0.001

i = i - 0.001
print i