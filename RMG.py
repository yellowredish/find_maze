from collections import deque
import random

# 장애물을 미로에 추가하기
def obstacle_func(miro, n):
    obstacles = (n-2)*(n-2)
    tmp = []
    for _ in range(obstacles):
        x, y = random.randint(1, n), random.randint(1, n)
        tmp.append([x, y])
    for x, y in tmp:
        miro[x][y] = 5 # 장애물 설치

    miro[1][1] = 0 # 시작지점
    miro[n][n] = 0 # 도착지점

# 시작과 도착이 이어져 있는지 확인하는 함수
def bfs(x, y, miro, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append([x, y])

    visited = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    visited[x][y] = 1  # 시작 지점을 방문한 것으로 마크

    while q:
        x, y = q.popleft()
        if x == n and y == n:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n and visited[nx][ny] == 0 and miro[nx][ny] != 5:
                visited[nx][ny] = 1  # 이동한 부분 마크
                q.append([nx, ny])
    return False

def change5to1(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 5:
                maze[i][j] = 1

def maze_func(n):
    maze = False
    while 1:
        # 모든 부분 이동할 수 없는 벽(1)로 채우기
        miro = [[1 for _ in range(n + 2)] for _ in range(n + 2)]
        # 캐릭터가 이동할 공간 전부 0으로 채워주기
        for i in range(1, n + 1): # 범위는 1 ~ n
            for j in range(1, n + 1):
                miro[i][j] = 0

        # 장애물 생성
        obstacle_func(miro, n)

        # 시작지점과 도착지점의 상하좌우 연결 확인
        maze = bfs(1, 1, miro, n)

        # 시작지점과 도착지점이 잘 연결되어 있다면 반복문 종료
        if maze == True:
            break
    
    change5to1(miro)
    # 미로 출력
    print(miro)

# n은 반드시 2 이상의 정수이어야 한다.
n = 100
maze_func(n)