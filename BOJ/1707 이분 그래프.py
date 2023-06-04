import sys
import collections


def bfs(cur_v):
    q = collections.deque()
    q.append(cur_v)
    C[cur_v] = 1
    while q:
        cur_v = q.popleft()
        for nxt_v in ad[cur_v]:
            if not C[nxt_v]:
                q.append(nxt_v)
                C[nxt_v] = C[cur_v] + 1


K = int(input())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    ad = [[] for i in range(V)]
    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        ad[u - 1].append(v - 1)
        ad[v - 1].append(u - 1)
    C = [0 for j in range(V)]
    ans = True
    for i in range(V):
        if not C[i]:
            bfs(i)
    for i in range(V):
        for j in ad[i]:
            if C[i] == C[j]:
                print("NO")
                ans = False
                break
        if not ans:
            break
    if ans:
        print('YES')