#Matrix 46
import random
N = 3
M = 3
x = 0
matrix = []
for i in range(N):
    matrix.append([])
    for j in range(M):
        matrix[i].append(random.randint(0,10))
print("Матрица M x N: ", matrix)
for i in range(N):
    min = 11
    max = 0
    for j in range(M):
       if max<matrix[i][j]:
            max = matrix[i][j]
            stroka = j
    for k in range(N):
        if min>matrix[k][stroka]:
            min = matrix[k][stroka]
    if min == max:
        x = min
print("Ответ:",x)
        