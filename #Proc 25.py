sum = 0
K = [1, 25, 16, 8, 7, 81, 91, 33, 67, 22]
def IsSquare(K):
    global t
    t = bool(False)
    i = int(1)
    while K >= i*i:
        if K == i*i:
            t = bool(True)
        i = i+1
    return t
for k in range(0,10):
    print(IsSquare(K[k]))
    if t == True:
        sum = sum + 1
print(sum)
