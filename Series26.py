# Series 26
K = int(input())
N = int(input())
A = [0]*N
for i in range(N):
	A[i] = int(input())
	A[i] = A[i]**K
print("Новые числа:")
print(A)
