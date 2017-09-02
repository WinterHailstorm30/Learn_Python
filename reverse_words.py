s = input('your sentence: ')

result = ' '.join(w[::-1] for w in s.split())
print(result)