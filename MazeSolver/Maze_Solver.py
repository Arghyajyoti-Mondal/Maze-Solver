import os
os.system('cls')

import time
from collections import deque
import matplotlib.pyplot as plt

# Load the maze from the text file
def load_maze(file_path):
    maze = []
    with open(file_path, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

# Find the coordinates of the start and goal states
def find_start_goal(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start = (row, col)
            elif maze[row][col] == 'G':
                goal = (row, col)
    return start, goal


def get_maze_size(maze):
    size=0
    for rows in range(len(maze)):
        for columns in range(len(maze[rows])):
            if (maze[rows][columns]=='*'):
                size+=1
    return size


# Define actions (Left, Right, Up, Down) 
#for mapping.
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
action_names = ['Left', 'Right', 'Up', 'Down']

# Breadth First Search
def bfs(maze, start, goal):
    queue = deque([(start, [])])
    visited = set() #to avoid duplicate values

    start_time = time.time()

    while queue: # means loop until the queue is empty
        current, path = queue.popleft() #FIFO
        row, col = current #unpacking the coordinates.

        if current == goal: #return when current==g
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i] #mapping action to action name
            new_row, new_col = row + action[0], col + action[1] #shifting coordinate --> moving to a particular direction.
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited: #checking 4 conditions.
                '''
                0 <= new_row < len(maze) #checks if row is in proper range.
                0 <= new_col < len(maze[0]) #checks if columns is in proper range.
                maze[new_row][new_col] != '#' #boundary check
                new_pos not in visited #visited coordinates should not be traversed again.
                '''
                visited.add(new_pos) #add new position in visited if it ssatisfy all the condition.
                queue.append((new_pos, path + [action_name])) 
                # print("\n")
                # print("\n")
                # print("\n")
                # print(queue)


    return "Path not found", time.time() - start_time

# Depth First Search
def dfs(maze, start, goal):
    stack = [(start, [])]
    visited = set()

    start_time = time.time()

    while stack:
        current, path = stack.pop()
        row, col = current

        if current == goal:
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i]
            new_row, new_col = row + action[0], col + action[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                stack.append((new_pos, path + [action_name]))

    return "Path not found", time.time() - start_time

# Uniform Cost Search
def ucs(maze, start, goal):
    queue = [(0, start, [])]
    visited = set()

    start_time = time.time()

    while queue:
        cost, current, path = queue.pop(0)
        row, col = current

        if current == goal:
            end_time = time.time()
            return path, end_time - start_time

        for i in range(len(actions)):
            action, action_name = actions[i], action_names[i]
            new_row, new_col = row + action[0], col + action[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#' and new_pos not in visited:
                visited.add(new_pos)
                new_cost = cost + 1  # Uniform cost for all actions
                queue.append((new_cost, new_pos, path + [action_name]))
                queue.sort()  # Sort the queue based on cost

    return "Path not found", time.time() - start_time



# Function to plot maze size vs running time
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


# Function to print the maze with the path marked by "+"
def print_path_on_maze(maze, path):
    marked_maze = [list(row) for row in maze]

    row, col = start  # Initialize row and col to the starting position

    for action in path:
        if action == 'Left':
            marked_maze[row][col] = '+'
            col -= 1 #column is decreased while traversing left
        elif action == 'Right':
            marked_maze[row][col] = '+'
            col += 1 #column is incremented while traversing right
        elif action == 'Up':
            marked_maze[row][col] = '+'
            row -= 1 #row is increamented while traversing up
        elif action == 'Down':
            marked_maze[row][col] = '+'
            row += 1 #row is decremented while traversing down
    
    #printing the maze after joining the elements of the rows.
    for row in marked_maze:
        print(" ".join(row))

# Main function
if __name__ == '__main__':
    maze = load_maze("maze5.txt")
    start, goal = find_start_goal(maze)

    size=get_maze_size(maze)


    bfs_path, bfs_time = bfs(maze, start, goal)
    print("BFS Path:", bfs_path)
    print("BFS Running Time:", bfs_time)
    if bfs_path != "Path not found":
        print("\nBFS Path on Maze:\n")
        print_path_on_maze(maze, bfs_path)

    dfs_path, dfs_time = dfs(maze, start, goal)
    print("DFS Path:", dfs_path)
    print("DFS Running Time:", dfs_time)
    if dfs_path != "Path not found":
        print("\nDFS Path on Maze:\n")
        print_path_on_maze(maze, dfs_path)

    ucs_path, ucs_time = ucs(maze, start, goal)
    print("UCS Path:", ucs_path)
    print("UCS Running Time:", ucs_time)
    if ucs_path != "Path not found":
        print("\nUCS Path on Maze:\n")
        print_path_on_maze(maze, ucs_path)


   