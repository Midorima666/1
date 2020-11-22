#Matrix 19
import random
N = 3
M = 4
matrix = []
for i in range(N):
    matrix.append([])
    sum = 0
    for j in range(M):
        matrix[i].append(random.randint(0,10))
        sum = sum + matrix[i][j]
    print("Сумма эллементов",i, "строки: ",sum)
print("Матрица M x N: ", matrix)
