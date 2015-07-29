from datetime import date

sundays = 0
for year in xrange(1901,2001,1):
    sundays += sum([ 1 for month in xrange(1,13) if date(year,month,1).weekday() == 6 ])
print sundays
