N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_ = 10 ** 10
for a in A:
    for b in B:
        min_ = min(min_, A[i] -B[j])

# acc ツール
# oj ツール

