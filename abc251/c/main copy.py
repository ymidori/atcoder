from collections import deque


N = int(input())

S_store = set([])
max_ = -1
max_idx = -1
for i in range(1, N + 1):
    S, T = input().split()
    T = int(T)
    if S not in S_store:
        if max_ < T:
            max_idx = i
            max_ = T
    S_store.add(S)

