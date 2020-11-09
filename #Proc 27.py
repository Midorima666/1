sum = 0
K = [1, 8, 16, 8, 7, 81, 91, 2, 67, 22]
def IsPoverN(K,N):
    global sum
    i = 0
    while N**i < K:
        i = i + 1
    if K==N**i:
        sum = sum + 1
        return True
    else:
        return False
for i in range(0,10):
    print(IsPoverN(K[i],2))
print(sum)
