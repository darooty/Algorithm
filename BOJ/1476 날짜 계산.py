E, S, M = map(int, input().split())
ans = 1


def test(n):
    for d, r in [(15, E), (28, S), (19, M)]:
        if (n - 1) % d + 1 != r:
            return False
    return True


while True:
    if test(ans):
        print(ans)
        break
    ans += 1