def findFactSum(N):
    f = 1
    Sum = 0
    for i in range(1, N + 1):
        f = f * i
        Sum += f
    return Sum
N=int(input('enter number:'))
print('sum of factorials is:',findFactSum(N))
  
