N = int(input())
# T, K, *A = [list(map(int, input().split())) for cnt in range(N)]
T = []
K = []
A = []
for cnt in range(N):
    T_, K_, *A_ = list(map(int, input().split()))
    T.append(T_)
    K.append(K_)
    A.append(A_)
# print(f"{T}, {K}, {A}")
time = 0
skill_needed = [False] * (N) 
skill_needed.append(True)
for i in range(0, N + 1)[::-1]:
    # print(i)
    if skill_needed[i] == True:
        time += T[i - 1]
        for j in A[i - 1]:
            skill_needed[j] = True
print(time)

