lower = 1
upper = 100
sum = 0
print "Sum of Prime numbers between", lower, "and", upper, "are:"

for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
           sum = sum + num

print "Total sum ", sum