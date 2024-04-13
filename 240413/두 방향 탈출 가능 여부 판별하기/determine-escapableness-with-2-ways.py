import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

def dfs(x, y):
    visited[x][y] = 1
    if x == n and y < m:
        if visited[x][y+1] == 0 and graph[x][y+1] == 1:
            dfs(x, y+1)
    elif x < n and y == m:
        if visited[x+1][y] == 0 and graph[x+1][y] == 1:
            dfs(x+1, y)
    elif x != n and y != m:
        if visited[x][y+1] == 0 and graph[x][y+1] == 1:
            dfs(x, y+1)
        if visited[x+1][y] == 0 and graph[x+1][y] == 1:
            dfs(x+1, y)

graph = [[]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    graph[i].insert(0,0)

visited = [[0]*(m+1) for _ in range(n+1)]
dfs(1,1)
print(1 if visited[n][m] == 1 else 0)