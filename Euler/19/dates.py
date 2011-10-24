months = [['Jan',31], ['Feb',28], ['Mar',31], ['Apr',30], ['May',31],['Jun',30], ['Jul',31], ['Aug',31], ['Sep',30], ['Oct',31], ['Nov',30], ['Dec',31]]

def isLeap(year):
  if year%4 == 0:
    if year%100 == 0:
      if year%400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def countDays():
  month = 'Jan'
  dayOfWeek = 0
  num = 0

  for i in range(1900, 2001):
    for mon in months:
      days = mon[1]
      if mon[0] == 'Feb' and isLeap(i):
        days =  days + 1
      dayOfWeek = (dayOfWeek + days)%7
      if (mon[0] == 'Dec' and i == 1900)   or (i > 1900 and not (i == 2000 and mon[0] == 'Dec')):
        if(dayOfWeek == 6):
          num += 1
  print num

for mon in months:
  print mon[0] + str(mon[1])

countDays()
      
