year = int(input())
# Displays a year is Leap year or not
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print "{0} is a leap year".format(year)
       else:
           print "{0} is not a leap year".format(year)
   else:
       print "{0} is a leap year".format(year)
else:
   print "{0} is not a leap year".format(year)