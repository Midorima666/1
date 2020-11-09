A = [1,2,3,4]
N = len(A)
B = []
SUM = sum(A)
for K in range(0, N):
    B.append(SUM)
    SUM = SUM - A[K]
print(B)