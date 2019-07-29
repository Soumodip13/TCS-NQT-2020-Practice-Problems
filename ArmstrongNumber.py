num = int(input("Enter a number: "))
# Initialising sum as 0
sum = 0
temp = num
# while the value of temp is greater than 0 the loop will continue
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print num,"is an Armstrong number"
else:
   print num,"is not an Armstrong number"