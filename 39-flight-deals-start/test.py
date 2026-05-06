
from datetime import date, timedelta

d1 = date(2008,8,15)
d2 = date(2008,9,15)

# you can't join dates, so if you want to use join, you need to
# cast to a string in the list comprehension:
ddd = [str(d1 + timedelta(days=x)) for x in range((d2-d1).days + 1)]
# now you can join
dates = (", ".join(ddd))
print(dates)
print(type(dates))