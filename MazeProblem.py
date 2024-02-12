import random
from queue import Queue

def create_maze(dim):
    maze = [[1 for _ in range(dim*2+1)] for _ in range(dim*2+1)]
    x, y = 0, 0
    maze[2*x+1][2*y+1] = 0
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < dim and 0 <= ny < dim and maze[2*nx+1][2*ny+1] == 1:
                maze[2*nx+1][2*ny+1] = 0
                maze[x+dx+x+1][y+dy+y+1] = 0
                stack.append((nx, ny))
    maze[1][0] = 0  # Entrance
    maze[-2][-1] = 0  # Exit
    return maze

def find_path_bfs(maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start, end = (1, 0), (len(maze)-2, len(maze[0])-1)
    visited = [[False for _ in row] for row in maze]
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        (node, path) = queue.get()
        if node == end:
            return path
        for dx, dy in directions:
            next_node = (node[0]+dx, node[1]+dy)
            if 0 <= next_node[0] < len(maze) and 0 <= next_node[1] < len(maze[0]) and maze[next_node[0]][next_node[1]] == 0 and not visited[next_node[0]][next_node[1]]:
                visited[next_node[0]][next_node[1]] = True
                queue.put((next_node, path + [next_node]))

def print_maze(maze, path=None):
    path_set = set(path) if path else set()
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print("·", end="")  # Path
            elif cell == 1:
                print("█", end="")  # Wall
            else:
                print(" ", end="")  # Open space
        print() 
dim = 10
maze = create_maze(dim)
path = find_path_bfs(maze)
print_maze(maze, path)

# 3 String Operations 
def StringOperator(string, operations):
    letters = list(string)  # Converting string into a list of characters
    output = []

    for operation in operations:
        if operation == 'R':
            letters = letters[::-1]  # Reversing the string
        elif operation == 'P':
            if letters:  # Checking if the letters list is not empty
               output.append(letters.pop(0))

    output.extend(letters)     # Appending the remaining letters from the input string to the output list
    return ''.join(output)    # Using the .join method to join the elements of the output list into a string.

# Testing the code
print(StringOperator("1soloCIPC", "RPPRPRPRPRPPRPP"))
print(StringOperator("dWW397uyFw6qiKVEXpGwD57FVtwp2Ltg2plqcVUh6zZZKQ3cvtihvYvGnf58yVVbJVPD3VuLqi9Fj1EuLFzvTRnLmzdtI7As5HSQ", "PRPPPRRRPPPRPPRRPRRPRRPRPPRPPRPPRPRPPRPRPPRPPPRRRPPRPRRRPRRRRRPRPRPPPPRPRPRRPPRPPRRRRPRPPRRRPRPRRPPPRPRRPRPRPPRRRRPPPPPPPRPRPPPPRPPRPPRRPPPRRPPRRRPPPRPRPPPRPRRPRRRPPPPPRRRRRRRPRPRRRPPRPRRPPPRRRRP"))


