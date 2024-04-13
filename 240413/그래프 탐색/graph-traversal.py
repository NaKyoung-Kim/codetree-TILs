import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

result = 0
visited = [0]*(N+1)
def dfs(v, visited, result):
    queue = deque([v])
    visited[v] = 1
    while queue:
        n = queue.popleft()
        for i in range(N+1):
            if graph[n][i] == 1 and visited[i] == 0:
                queue.append(i)
        if visited[n] == 0:
            visited[n] = 1
            result += 1
    return result

print(dfs(1, visited, result))