def dfs(depth, cur_v):
    find = False
    V[cur_v] = 1
    depth += 1
    if depth == 5:
        return True
    for nxt_v in ad[cur_v]:
        if not V[nxt_v]:
            find = dfs(depth, nxt_v)
            if find:
                return find
            V[nxt_v] = 0
    return find


N, M = map(int, input().split())
ad = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    ad[a].append(b)
    ad[b].append(a)
V = [0 for _ in range(N)]
find = False
for cur_v in range(N):
    find = dfs(0, cur_v)
    V[cur_v] = 0
    if find:
        print(1)
        break
if not find:
    print(0)
