s = input('your phrase: ')

import string
s1 = s.replace(' ', '')
s2 = s1.translate(str.maketrans('','',string.punctuation))
s3 = s2.lower()

s3Rev = reversed(s3)
if list(s3) == list(s3Rev):
	print("YES")
else:
	print("NO")