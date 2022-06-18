N = int(input())
TKA = [list(map(int, input().split())) for cnt in range(N)]
time = 0
skill_list = []
for i in range(2, TKA[N - 1][1] + 2):
    # time += TKA[TKA[N-1][i] - 1][0]
    skill_list = skill_list + TKA[TKA[N-1][i] - 1][2:]
skill_list = list(set(skill_list + TKA[N - 1][2:]))
print(skill_list)
for skill in skill_list:
    time += TKA[skill - 1][0]
print(time + TKA[N-1][0])
