#Minmax 29
import random
N = 10
k = 6
sum = 0
nabor = []
for i in range(N):
    nabor.append(random.randint(0,5))
print("Набор: ", nabor)
for i in range(1, N-1):
    if (nabor[i]<=nabor[i-1]) and (nabor[i]<=nabor[i+1]) and (nabor[i]<=k):
        if (nabor[i]==nabor[i-1]) and (k==nabor[i]):
            sum = sum + 1
        elif nabor[i]!=k:
            sum = 1
        k = nabor[i]
if k == 6:
    print("Минимума нет")  
else:
    print("Количество:", sum)