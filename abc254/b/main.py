n = int(input())
a_list = []
for i in range(n):
    if i == 0:
        print("1")
    elif i == 1:
        a_list = ["1", "1"]
        print(' '.join(map(str, a_list)))
    else:
        a_list_bf = a_list.copy()
        a_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                a_list.append("1")
            else:
                aij = int(a_list_bf[j-1]) + int(a_list_bf[j])
                a_list.append(str(aij))
        print(' '.join(map(str, a_list)))
