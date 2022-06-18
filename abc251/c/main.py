# from logging import debug
N = int(input())
S = set([])
M = N + 1
max = -1
max_idx = -1
for _ in range(1, M):
    S_, T_ = input().split()
    T_ = int(T_)
    if S_ not in S:
        if T_ > max:
            max = T_
            max_idx = _
        S.add(S_)
# print(S)
print(max_idx)
