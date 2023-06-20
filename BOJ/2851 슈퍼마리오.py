N = [int(input()) for _ in range(10)]
E = []
rlt = 0
diff = 100
ans = -1
for i in range(10):
    rlt += N[i]
    E.append(rlt)
for i in range(10):
    if abs(100 - E[i]) <= diff:
        diff = abs(100 - E[i])
        ans = E[i]
print(ans)