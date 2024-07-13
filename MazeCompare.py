import matplotlib.pyplot as plt
import time
from DFS import dfs_find
from BFS import bfs_find
from OneAnswerRMG import generate_maze

CASES = 10
for n in range(CASES):
    WIDTH, HEIGHT = 200, 200
    print(f"maze {n} generating...")
    oneway_maze = generate_maze(WIDTH, HEIGHT)
    print(f"maze {n} generated")
    
    REPEATS = 10
    for i in range(REPEATS):
        ave_record = 0
        timestamp = time.time()
        dfs_find(oneway_maze)
        currecord = time.time() - timestamp
        ave_record += currecord / REPEATS
        print("DFS", i+1, currecord)

    if n: plt.plot(i, ave_record, 'ro')
    else: plt.plot(i, ave_record, 'ro', label="DFS")

    for i in range(REPEATS):
        ave_record = 0
        timestamp = time.time() 
        bfs_find(oneway_maze)
        currecord = time.time() - timestamp
        ave_record += currecord / REPEATS
        print("BFS", i+1, currecord)

    if n: plt.plot(i, ave_record, 'bo')
    else: plt.plot(i, ave_record, 'bo', label="BFS")


plt.title('Time compare between DFS and BFS')
plt.xlabel('CASE')
plt.ylabel('TIME')
plt.legend(loc='upper right')
plt.show()