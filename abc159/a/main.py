n, m = map(int, input().split())
res = 0
for i in range(1, n):
    res += i
for j in range(1, m):
    res += j
print(res)
