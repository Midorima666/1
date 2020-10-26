# Series 5
N = int(input())
S = 0
A = [0]*N
for i in range(N):
	A[i] = float(input())
	A[i] = int(A[i])
	S = S + A[i]
print("Новые числа:")
print(A)
print("Cóмма:")
print(S)
