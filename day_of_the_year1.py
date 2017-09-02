month = int(input('month: '))
day = int(input('day: '))
year = int(input('year: '))

def isLeapYr(year):
    if(year % 4) == 0:
        if(year % 100) == 0:
            if(year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if isLeapYr(year) == True:
    LeapYr = 1
if isLeapYr(year) == False:
    LeapYr = 0

if month == 1:
    print(day)
elif month == 2:
    print(31 + day)
elif month == 3:
    print(59 + day + LeapYr)
elif month == 4:
    print(90 + day + LeapYr)
elif month == 5:
    print(120 + day + LeapYr)
elif month == 6:
    print(151 + day + LeapYr)
elif month == 7:
    print(181 + day + LeapYr)
elif month == 8:
    print(212 + day + LeapYr)
elif month == 9:
    print(243 + day + LeapYr)
elif month == 10:
    print(273 + day + LeapYr)
elif month == 11:
    print(304 + day + LeapYr)
elif month == 12:
    print(334 + day + LeapYr)