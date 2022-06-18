R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for i in range(R)]

sy -= 1 # 1 index 
sx -= 1 # 1 index

counts = [[-1] * C for _ in range(R)]
counts[sy][sx] = 0

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
queue = [(sy, sx)]
while queue:
    current_y, current_x = queue.pop(0)
    count = counts[current_y][current_x]
    for dy, dx in directions:
        new_y = current_y + dy
        new_x = current_x + dx

        if c[new_y][new_x] == "#":
            continue
        if counts[new_y][new_x] != -1:
            continue

        counts[new_y][new_x] = count + 1
        queue.append((new_y, new_x))
