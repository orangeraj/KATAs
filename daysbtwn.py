import datetime

date1 = '31-1'
date2 = '4-8'

date1s = date1.split('-')
date2s = date2.split('-')

#y = datetime.datetime.now()
x = datetime.datetime(2020,int(date1s[1]),int(date1s[0]))
y = datetime.datetime(2020,int(date2s[1]),int(date2s[0]))

z = y - x
print(z.days)