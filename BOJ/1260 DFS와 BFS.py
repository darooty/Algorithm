import collections


def dfs(cur_v, grp):
    C[cur_v] = grp
    print(str(cur_v + 1),end=' ')
    for nxt_v in ad[cur_v]:
        if C[nxt_v] != grp:
            dfs(nxt_v, grp)


def bfs(cur_v, grp):
    q = collections.deque()
    q.append(cur_v)
    C[cur_v] = grp
    while q:
        cur_v = q.popleft()
        print(cur_v + 1, end=' ')
        for nxt_v in ad[cur_v]:
            if C[nxt_v] != grp:
                q.append(nxt_v)
                C[nxt_v] = grp


N, M, V = map(int, input().split())
ad = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    ad[a - 1].append(b - 1)
    ad[b - 1].append(a - 1)
for i in range(N):
    ad[i] = sorted(ad[i])
C = [0 for _ in range(N)]
dfs(V - 1, 1)
print()
bfs(V - 1, 2)
