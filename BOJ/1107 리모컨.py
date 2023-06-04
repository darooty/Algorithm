# 22:44

N = int(input())
M = int(input())
if M:
    A = list(map(int, input().split()))
else:
    A = []
B = []
for a in range(10):
    if a not in A:
        B.append(a)
ans = abs(N - 100)


def cal_dist(n, rlt):
    return n + abs(N - int(rlt))


def go(cnt, rlt):
    global ans
    if 0 < cnt <= 6:
        ans = min(ans, cal_dist(cnt, rlt))
    if cnt == 6:
        return
    for b in B:
        if rlt == '0' and not b:
            continue
        rlt += str(b)
        go(cnt + 1, rlt)
        rlt = rlt[:-1]


go(0, '')
print(ans)
