# if 12
a = int(input())
b = int(input())
c = int(input())
if a != b and b != c and a != c:
	if a < b and a < c:
		print(a)
	else:
		if b < a and b < c:
			print(b)
		else:
			print(c)
else:
	if c == b and b == c:
		print(b)
	else:
		if a == b:
			if a < c:		
				print(a)
			else:
				print(c)
		if c == b: 
			if c < a:
				print(c)
			else:
				print(a)
		if a == c: 
			if a < b:		
				print(a)
			else:
				print(b)
