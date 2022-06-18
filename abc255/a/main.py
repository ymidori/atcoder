R, C = map(int, input().split())
R = R - 1
C = C - 1
A = []
A_1 = list(map(int, input().split()))
A_2 = list(map(int, input().split()))
A.append(A_1)
A.append(A_2)
print(A[R][C])
# print(R)
# print(C)
