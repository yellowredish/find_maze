from random import randrange

def generate_maze(n):
    from DFS import dfs_find
    
    q = 0
    while True:
        maze = [[1 for _ in range(n+2)] for _ in range(n+2)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                maze[i][j] = 0 if randrange(2) else 1

        print(q)
        maze[1][1] = maze[n-1][n-1] = 0
        maze[2][1] = maze[1][2] = maze[n-2][n-1] = maze[n-1][n-2] = 0

        rslt = dfs_find(maze)
        print(q)
        q += 1
        if len(rslt) != 1:
            return maze


if __name__ == "__main__":
    maze = generate_maze(200)
    print(maze)