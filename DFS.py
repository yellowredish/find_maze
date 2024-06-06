z = [
    [1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1],
[1, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1]
]
visited = []
stack = []
def dfs(x, y, maze, goal):
    lenx = len(maze[0])
    leny = len(maze)

    

    if x == goal[0] and y == goal[1]:
        
        return stack
    
    dx = [0,0,-1,1] # 상 하 좌 우
    dy = [1,-1,0,0]

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i] 
        if (next_x > 0 and 
            next_y > 0 and
            next_x < lenx-1 and 
            next_y < leny-1):
            if maze[next_y][next_x] == 0 and [next_x,next_y] not in visited :
                visited.append([next_x,next_y])
                stack.append([next_x,next_y])
                dfs(next_x, next_y, maze, goal)
        
   

dfs(1,1,z,[5,5])     
print(visited)  
                
        
                


