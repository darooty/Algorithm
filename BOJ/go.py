import math

N = int(input())
n = int(math.sqrt(N))
E = [i for i in range(n, 0, -1)]
size = len(E)
ans = 5


def go(start, cnt, rlt):
    global ans
    if rlt == N:
        ans = min(ans, cnt)
    if cnt == 4:
        return
    for i in range(start, size):
        go(i+1, cnt+1, rlt+E[i]**2)
a=1
go(0, 0, 0)
print(ans)
