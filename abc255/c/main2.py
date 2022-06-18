X, A, D, N = map(int, input().split())

# start end を作り、start を 0 に合わせる
start = A
end = D * (N - 1) + A
if start > end:
    start, end = end, start
    D = abs(D)
if X <= start:
    print(start - X)
    exit()
if end <= X:
    print(X - end)
    exit()
# start -= start
# end -= start
X -= start
mod = X % D
print(min(mod, D - mod))
