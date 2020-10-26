# While 6
N = int(input())
a = 1
if N % 2 == 0:
	while N >= 2:
		a = a*N
		N = N - 2
else:
	while N >=1:
		a = a*N
		N = N -2
print(a)
