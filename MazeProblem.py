from queue import Queue

class MazeSolver:
    def __init__(self, maze, destination):
        self.maze = maze
        self.destination = destination

    def find_path(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        start = (0, 0)
        queue = Queue()
        queue.put((start, [start]))  # (current position, path so far)
        visited = set([start])

        while not queue.empty():
            current_pos, path = queue.get()
            if current_pos == self.destination:
                return path  # Return the path if destination is reached

            x, y = current_pos
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.put(((nx, ny), path + [(nx, ny)]))
                    visited.add((nx, ny))

        return None  # If no path is found

def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        maze = [[int(num) for num in line.strip()] for line in lines[:-1]]
        destination = tuple(map(int, lines[-1].strip().split(',')))
    return maze, destination

# Example usage
if __name__ == "__main__":
    # Replace 'MazeSamples.txt' with the actual path to your file
    filename = 'MazeSamples.txt'
    maze, destination = read_maze_from_file(filename)

    solver = MazeSolver(maze, destination)
    path = solver.find_path()

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
