yourNumber = int(input('number: '))
yourNumberCopy = str(yourNumber)

if yourNumber == 1:
	print("unit")
	exit()

if yourNumber < 1:
	print("number has to be positive")
	exit()

for x in list(range(2, yourNumber - 1)):
	if yourNumber % x == 0:
		print(yourNumberCopy + " is composite.")
		exit()

print(yourNumberCopy + ' is prime.')