from collections import deque


def bfs_find(maze: list[list[int]]): #정사각형의 미로에서 작동
    n = len(maze)
    initx, inity = 1, 1
    visited = [[False for _ in range(n)] for _ in range(n)]
    prev_vertex = [[(0, 0) for _ in range(n)] for _ in range(n)]

    q = deque([(initx, inity)])
    visited[inity][initx] = True
    prev_vertex[inity][initx] = (inity, initx)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        if x == y == n: break

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not (0 < next_x < n and 0 < next_y < n): continue
            if visited[next_y][next_x] or maze[next_y][next_x] == 1: continue

            visited[next_y][next_x] = True
            q.append((next_x, next_y))
            prev_vertex[next_y][next_x] = (y, x)

    route = [prev_vertex[n-2][n-2]]
    while route[-1] != (inity, initx):
        x, y = route[-1]
        route.append(prev_vertex[x][y])
        #print(route)

    route.reverse()
    route.append((n-2, n-2))
    return route


if __name__ == "__main__":
    maze = [[1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1]]
    
    route = bfs_find(maze)
    print("BFS: ", route)