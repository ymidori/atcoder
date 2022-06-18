import sys


def debug(*args, end="\n"):
    print(*args, end=end, file=sys.stderr)


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]
XY = [list(map(int, input().split())) for _ in range(N)]
debug(f"{A=}")
debug(f"{XY=}")
dist_min = []
for i in range(N):
    tmp = []
    for j in A:
        x1 = XY[j][0]
        y1 = XY[j][1]
        x2 = XY[i][0]
        y2 = XY[i][1]

        dist = (x1-x2)**2 + (y1-y2)**2
        tmp.append(dist)
    dist_min.append(min(tmp))
print(pow(max(dist_min), 0.5))
