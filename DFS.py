import sys
sys.setrecursionlimit(1000000)



def dfs_find(maze: list[list[int]]): #정사각형의 미로에서 작동
    n = len(maze) - 2
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    visited[1][1] = True
    route = [(1, 1)]

    def dfs(x, y, maze, n):
        if x == y == n: # 답을 찾았을 경우
            return True
        
        dx = [0,0,-1,1] # 상 하 좌 우
        dy = [1,-1,0,0]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if not (0 < next_x <= n and 0 < next_y <= n): continue
            if visited[next_y][next_x] or maze[next_y][next_x] == 1: continue

            visited[next_y][next_x] = True
            route.append((next_y, next_x))
            if dfs(next_x, next_y, maze, n): return True
            route.pop()
            visited[next_y][next_x] = False

        return False
    
    dfs(1, 1, maze, n)

    return route

if __name__ == "__main__":
    maze = [[1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1]]
    
    route = dfs_find(maze)
    print("DFS: ", route)
