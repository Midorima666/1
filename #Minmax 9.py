#Minmax 9
import random
N = 10
k = 0
nabor = []
for i in range(N):
        nabor.append(random.randint(0,10))
print("Набор: ", nabor)
for i in range(1, N-1):
    if (nabor[i]>nabor[i-1]) and (nabor[i]>nabor[i+1]):
        if k == 0:
            print("Номер первого макс. элемента:", i)
            k = i
        else:
            k = i
print("Номер последнего макс. элемента:", k)
