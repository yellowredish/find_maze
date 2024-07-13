import matplotlib.pyplot as plt
import time
from DFS import dfs_find
from BFS import bfs_find
from OneAnswerRMG import generate_maze

CASES = 10
FIRST = 0
for n in range(CASES):
    dfsave = bfsave = 0
    MAZECOUNT = 10
    for k in range(MAZECOUNT):
        WIDTH, HEIGHT = 20*(n+1), 20*(n+1)
        print(f"maze {n+1}/{CASES} generating...")
        oneway_maze = generate_maze(WIDTH, HEIGHT)
        print(f"maze {n+1}/{CASES} generated")

        REPEATS = 5
        for i in range(REPEATS):
            ave_record = 0
            timestamp = time.time()
            dfs_find(oneway_maze)
            currecord = time.time() - timestamp
            ave_record += currecord / REPEATS
            print("DFS", k+1, i+1, currecord)
        dfsave += ave_record / MAZECOUNT

        for i in range(REPEATS):
            ave_record = 0
            timestamp = time.time() 
            bfs_find(oneway_maze)
            currecord = time.time() - timestamp
            ave_record += currecord / REPEATS
            print("BFS", k+1, i+1, currecord)
        bfsave += ave_record / MAZECOUNT

    if n != FIRST: plt.plot(WIDTH, dfsave, 'ro')
    else: plt.plot(WIDTH, dfsave, 'ro', label="DFS")

    if n != FIRST: plt.plot(WIDTH, bfsave, 'bo')
    else: plt.plot(WIDTH, bfsave, 'bo', label="BFS")


plt.title('Time compare between DFS and BFS')
plt.xlabel('MAZE SIZE')
plt.ylabel('AVERAGE TIME')
plt.legend(loc='upper right')
plt.show()