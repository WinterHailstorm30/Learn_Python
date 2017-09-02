yourNumber = int(input('your number: '))
yourNumberCopy = str(yourNumber)

if yourNumber == 1:
	print(yourNumberCopy + " is unit.")
	exit()

if yourNumber < 1:
	print("number has to be positive")
	exit()

for x in list(range(2, round(yourNumber**(0.5)))):
	if yourNumber % x == 0:
		print(yourNumberCopy + " is composite.")
		exit()

print(yourNumberCopy + ' is prime.')