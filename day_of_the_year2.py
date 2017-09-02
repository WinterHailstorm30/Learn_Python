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

# print(isLeapYr(2013))

if isLeapYr(year) == True:
    LeapYr = 1
if isLeapYr(year) == False:
    LeapYr = 0

if month == 2 and day == 29 and LeapYr == 0:
    print("YOU CANNOT TRICK ZE ME!!!!!!!!!! THERE IS NO FEBURARY 29TH!!!!!!!!!! I AM ZE GOD!!!!!!!!!!")
    exit()

if month == 1 and day < 32:
    print(day)
elif month == 2 and day < 30:
    print(31 + day)
elif month == 3 and day < 32:
    print(59 + day + LeapYr)
elif month == 4 and day < 31:
    print(90 + day + LeapYr)
elif month == 5 and day < 32:
    print(120 + day + LeapYr)
elif month == 6 and day < 31:
    print(151 + day + LeapYr)
elif month == 7 and day < 32:
    print(181 + day + LeapYr)
elif month == 8 and day < 32:
    print(212 + day + LeapYr)
elif month == 9 and day < 31:
    print(243 + day + LeapYr)
elif month == 10 and day < 32:
    print(273 + day + LeapYr)
elif month == 11 and day < 31:
    print(304 + day + LeapYr)
elif month == 12 and day < 32:
    print(334 + day + LeapYr)
else:
    print("YOU CANNOT TRICK ZE ME!!!!!!!!!! I AM ZE GOD!!!!!!!!!!")