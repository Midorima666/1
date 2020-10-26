# for 21
N = int(input())
k = 1
b = 1
for c in range(1,N+1):
	b = b * c
	k = k + (1 / b)
print(k)
