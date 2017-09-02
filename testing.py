s = input('your sentence: ')

for w in s.split():
	result = ' '.join(w[::-1])
print(result)