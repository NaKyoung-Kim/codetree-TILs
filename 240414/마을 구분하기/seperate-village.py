import sys

n = int(sys.stdin.readline())
visited = [[0]*n for _ in range(n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

people_count = []
temp_people = 0

def in_range(new_x, new_y):
    return new_x >= 0 and new_y >= 0 and new_x < n and new_y < n

def can_go(x,y):
    return in_range(x,y) and visited[x][y] == 0 and graph[x][y] == 1

def dfs(x, y):
    global temp_people
    visited[x][y] = 1
    dxs = [-1, 0, 0, 1]
    dys = [0, -1, 1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            temp_people += 1
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            temp_people = 1
            dfs(i,j)
            people_count.append(temp_people)

print(len(people_count))
people_count.sort()
for count in people_count:
    print(count)