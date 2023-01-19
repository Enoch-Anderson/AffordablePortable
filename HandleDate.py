import datetime as dt

#create julian calender for leap year an non leap year
daysInMonthNoLeap = [0,31,28,31,30,31,30,31,31,30,31,30,31] #zero added so I don't have to do -1's later
daysInMonthWithLeap = [0,31,29,31,30,31,30,31,31,30,31,30,31]
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = dt.date.today()

def calcJulian(date: dt.datetime.date): 
    year = date.year
    month = date.month
    day = date.day
    output = 0
    # figure out if it is a leap year or not
    if year % 4 == 0: #it is a leap year
        months = daysInMonthWithLeap
    else:
        months = daysInMonthNoLeap
    i = 0
    while i != month:
        output += months[i]
        i += 1
    output += day
    return output

def makeJulDateClass(jul: int, year):
    if year%4==0: #it is a leap year
        months = daysInMonthWithLeap
    else:
        months = daysInMonthNoLeap
    i = 0
    while months[i] < jul:
        jul -= months[i]
        i += 1
    output = dt.date(year, i, jul)
    return output

def daysSinceCleaned(date):
    julDay = calcJulian(date)
    julToday = calcJulian(today)
    return julToday-julDay


x = dt.date(2022, 7, 18)
print(x.weekday())
print(daysOfWeek[x.weekday()])