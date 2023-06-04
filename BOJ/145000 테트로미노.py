def dfs(depth, cur_x, cur_y, rlt):
    global ans
    V[cur_x][cur_y] = 1
    rlt += A[cur_x][cur_y]
    depth += 1
    if depth == 4:
        ans = max(ans, rlt)
        return
    for dx, dy in direction:
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        if 0 <= nxt_x < N and 0 <= nxt_y < M and not V[nxt_x][nxt_y]:
            dfs(depth, nxt_x, nxt_y, rlt)
            V[nxt_x][nxt_y] = 0


def cal_sub(cur_x, cur_y):
    rlt = 0
    if 0 <= cur_x + 2 < N and 0 <= cur_y + 1 < M:
        rlt = max(rlt, A[cur_x][cur_y] + A[cur_x + 1][cur_y] + A[cur_x + 1][cur_y + 1] + A[cur_x + 2][cur_y])
    if 0 <= cur_x + 2 < N and 0 <= cur_y - 1 < M:
        rlt = max(rlt, A[cur_x][cur_y] + A[cur_x + 1][cur_y] + A[cur_x + 1][cur_y - 1] + A[cur_x + 2][cur_y])
    if 0 <= cur_x + 1 < N and 0 <= cur_y + 2 < M:
        rlt = max(rlt, A[cur_x][cur_y] + A[cur_x][cur_y + 1] + A[cur_x][cur_y + 2] + A[cur_x + 1][cur_y + 1])
    if 0 <= cur_x - 1 < N and 0 <= cur_y + 2 < M:
        rlt = max(rlt, A[cur_x][cur_y] + A[cur_x][cur_y + 1] + A[cur_x][cur_y + 2] + A[cur_x - 1][cur_y + 1])
    return rlt


N, M = map(int, input().split())
A = [list(map(int, input().split())) for n in range(N)]
V = [[0 for j in range(M)] for i in range(N)]
direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
ans = 0
for x in range(N):
    for y in range(M):
        dfs(0, x, y, 0)
        V[x][y] = 0
        ans = max(ans, cal_sub(x, y))
print(ans)
