N, K = map(int, input().split())
a = list(map(int, input().split()))
a_sorted = sorted(a.copy())
for i in range(N):
    if i+K == N-1:
        break
    else:
        while True:
            if a[i] <= a[i+K]:
                break
            else:
                tmp = a[i+K]
                a[i+K] = a[i]
                a[i] = tmp
                i = i - K
                if i == 0:
                    break
# print(a)
# print(a_sorted)
if a == a_sorted:
    print("Yes")
else:
    print("No")
