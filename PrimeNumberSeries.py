lower = 1
upper = 100

print "Prime numbers between",lower,"and",upper,"are:"
# Prints the Prime number Series
for num in range(lower,upper + 1):

   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)



