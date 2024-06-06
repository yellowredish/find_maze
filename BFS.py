from collections import deque


def bfs(maze: list[list[int]], n: int):
    initx, inity = 1, 1
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[initx][inity] = True
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque([(initx, inity)])
    route = []

    while q:
        x, y = q.popleft()
        route.append((x, y))

        if x == y == n:
            return route

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not (0 < next_x < n and 0 < next_y < n):
                continue
            if maze[next_x][next_y] == 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                q.append((next_x, next_y))