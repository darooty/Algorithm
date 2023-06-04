import sys
import collections


def bfs(cur_v):
    q = collections.deque()
    q.append(cur_v)
    V[cur_v] = 1
    while q:
        cur_v = q.popleft()
        for nxt_v in ad[cur_v]:
            if not V[nxt_v]:
                q.append(nxt_v)
                V[nxt_v] = 1


N, M = map(int, sys.stdin.readline().split())
ad = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ad[a - 1].append(b - 1)
    ad[b - 1].append(a - 1)
V = [0 for _ in range(N)]
ans = 0
for i in range(N):
    if not V[i]:
        bfs(i)
        ans += 1
print(ans)