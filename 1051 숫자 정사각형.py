N, M = map(int, input().split())
area = [list(map(int, input())) for _ in range(N)]
ans = 1
max_edge = max(N, M)
for edge in range(1, max_edge):
    find = False
    for x in range(N):
        for y in range(M):
            if 0 <= x+edge < N and 0 <= y+edge < M:
                if area[x][y] == area[x+edge][y] and area[x][y] == area[x][y+edge] and area[x][y] == area[x+edge][y+edge]:
                    ans = (edge+1)**2
                    find = True
                    break
        if find:
            break
print(ans)