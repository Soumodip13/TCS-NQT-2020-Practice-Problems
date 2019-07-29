from datetime import datetime
from datetime import date
datetime.today()
today = datetime.today()
print today
type(today)
todaydate = date.today()
print type(todaydate)
print todaydate.month
print todaydate.year
print todaydate.day
christmas = date(2019, 12, 25)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")

