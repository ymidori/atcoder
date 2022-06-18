N = int(input())
A = list(map(int, input().split()))
A_tuple = [(a, i) for i, a in enumerate(A, start=1)]
block = (2 ** N) // 2
res = min(max(A_tuple[block:]), max(A_tuple[:block]))
# print(A_tuple[block:])
# print(max(A_tuple[block:]))
# print(max(A_tuple[:block]))
print(res[1])
