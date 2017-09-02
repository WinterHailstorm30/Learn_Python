month = int(input('month: '))
day = int(input('day: '))
year = int(input('year: '))

if month > 12:
    print("That is not a valid month!")
    exit()

checkList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day > checkList[month - 1]:
    print("There are not that many days in your month!")
    exit()

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
    leapYr = 1
if isLeapYr(year) == False:
    leapYr = 0

if month == 2 and day == 29 and leapYr == 0:
    print("There is no Feburary 29th in your year!")
    exit()

daysList = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
numberOfDays = daysList[month - 1] + day
if month < 3:
    print(numberOfDays)
else:
    print(numberOfDays + leapYr)