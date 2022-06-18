import numpy as np

X, A, D, N = map(int, input().split())
# F = A + (D * N)
# if A == D:
#     S = np.array([A])
#     print(S)
# else:
#     S = np.arange(A, F + 1, D)
#     print(S)

diff = X - A
# print(diff)
if D * N >= 0:
    min = A
    max = D * N + A
elif D * N < 0:
    min = D * N + A
    max = A
if X <= min:
    res = abs(X - min)
elif X > min and X < max:
    if abs(X - min) >= abs(max - X):
        start = abs(max - X) // D * D + A
        S = np.arange(start, X, -D)
        res = abs(X - S[-1])
    elif abs(X - min) < abs(max - X):
        start = abs(X - min) // D * D + A
        S = np.arange(start, X, D)
        res = abs(X - S[-1])
elif X >= max:
    res = abs(max - X)

print(res)
