import os
os.system('cls')

import matplotlib.pyplot as plt

bfs_times=[0.0,0.0,0,0,0.02698]
dfs_times=[0.0,0.0,0.001462,0.016,24.370]
ucs_times=[0.0,0.0,0,0.1794,0.2161]
size=[28,33,66,277,7101,19943]

def plot_running_times(maze_sizes, bfs_times, dfs_times, ucs_times):
    plt.plot(maze_sizes, bfs_times, label='BFS')
    plt.plot(maze_sizes, dfs_times, label='DFS')
    plt.plot(maze_sizes, ucs_times, label='UCS')
    plt.xlabel('Maze Size (Number of Empty Cells)')
    plt.ylabel('Running Time')
    plt.title('Maze Size vs Running Time for Different Algorithms')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    bfs_times=[0.0,0.0,0,0,0,0.02698]
    dfs_times=[0.0,0.0,0,0.001462,0.016,24.370]
    ucs_times=[0.0,0.0,0,0,0.1794,.2161]
    size=[28,33,66,277,7101,19943]
    # print(size)
    plot_running_times(size, bfs_times, dfs_times, ucs_times)