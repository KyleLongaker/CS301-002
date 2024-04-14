## Group Memebers: Katelyn Juhl, Kyle Longaker 
from collections import defaultdict, deque

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = 'white'  # All vertices start as unvisited ('white')
        self.previous = None
        self.discovery_time = 0
        self.closing_time = 0

    def __repr__(self):
        return f'Vertex({self.label})'

class AdjacencyList:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def read_graph(self, filepath):
        try:
            with open(filepath, 'r') as file:
                _, _ = map(int, file.readline().split())  # Read vertices and edges count
                vertices = file.readline().strip().split(',')
                for vertex in vertices:
                    self.add_vertex(vertex)
                for line in file:
                    from_vertex, to_vertex = line.strip().split()
                    self.add_edge(from_vertex, to_vertex)
            return True
        except IOError:
            print("File could not be read.")
            return False

    def add_vertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)

    def add_edge(self, from_label, to_label):
        if from_label in self.vertices and to_label in self.vertices:
            self.vertices[from_label].neighbors.add(self.vertices[to_label])
            self.vertices[to_label].neighbors.add(self.vertices[from_label])  # Undirected graph

    # Depth-First Search (DFS) with O(V + E) complexity, where V is the number of vertices and E is the number of edges.
    def dfs(self):
        for vertex in self.vertices.values():
            vertex.color = 'white'
            vertex.previous = None
        self.time = 0
        for vertex in self.vertices.values():
            if vertex.color == 'white':
                self.dfs_visit(vertex)

    # Helper function for DFS
    def dfs_visit(self, vertex):
        vertex.color = 'gray'
        self.time += 1
        vertex.discovery_time = self.time
        for neighbor in vertex.neighbors:
            if neighbor.color == 'white':
                neighbor.previous = vertex
                self.dfs_visit(neighbor)
        vertex.color = 'black'
        self.time += 1
        vertex.closing_time = self.time

    # Breadth-First Search (BFS) with O(V + E) complexity, where V is the number of vertices and E is the number of edges.
    def bfs(self, start_label, end_label):
        if start_label not in self.vertices or end_label not in self.vertices:
            return False
        
        queue = deque([(self.vertices[start_label], [])])
        visited = set()
        
        while queue:
            current, path = queue.popleft()
            if current.label == end_label:
                return path + [(path[-1][1].label, end_label)] if path else [(start_label, end_label)]
            
            visited.add(current)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [(current.label, neighbor.label)]))
        
        return []

    def display_graph(self):
        for vertex in self.vertices.values():
            print(f"{vertex}: {list(v.label for v in vertex.neighbors)}")

# Example usage
if __name__ == "__main__":
    graph = AdjacencyList()
    if graph.read_graph("graph.txt"):
        print("Graph loaded successfully!")
        graph.display_graph()
        path_bfs = graph.bfs('A', 'E')
        print(f"BFS path from 'A' to 'E': {path_bfs}")
        graph.dfs()  # Run DFS on the entire graph
        print("DFS complete. Time stamps and tree:")
        for v in graph.vertices.values():
            print(f'{v.label}: Discovered at {v.discovery_time}, Finished at {v.closing_time}')
    else:
        print("Failed to load graph.")

############################################-----New Code----#########################################################

from collections import defaultdict, deque

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()  # Use a set to avoid duplicate edges
        self.color = 'white'  # All vertices start as unvisited ('white')
        self.previous = None
        self.discovery_time = 0
        self.closing_time = 0

    def __repr__(self):
        return f'Vertex({self.label})'

class AdjacencyList:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def read_graph(self, filepath):
        try:
            with open(filepath, 'r') as file:
                file.readline()  # Skip the first line (vertex and edge count)
                vertices = file.readline().strip().split(',')
                for vertex in vertices:
                    self.add_vertex(vertex.strip())
                for line in file:
                    from_vertex, to_vertex = line.strip().split()
                    self.add_edge(from_vertex, to_vertex)
            return True
        except IOError as error:
            print(f"Error reading file: {error}")
            return False

    def add_vertex(self, label):
        if label not in self.vertices:
            self.vertices[label] = Vertex(label)

    def add_edge(self, from_label, to_label):
        if from_label in self.vertices and to_label in self.vertices:
            self.vertices[from_label].neighbors.add(self.vertices[to_label])
            self.vertices[to_label].neighbors.add(self.vertices[from_label])

    def delete_vertex(self, label):
        if label in self.vertices:
            for neighbor in list(self.vertices[label].neighbors):
                neighbor.neighbors.remove(self.vertices[label])
            del self.vertices[label]
            return True
        return False

## Breadth-First Search (BFS) with O(V + E) complexity, where V is the number of vertices and E is the number of edges.
    def bfs(self, start_label, end_label):
        for vertex in self.vertices.values():
            vertex.color = 'white'
            vertex.previous = None
        queue = deque([self.vertices[start_label]])
        self.vertices[start_label].color = 'gray'
        while queue:
            vertex = queue.popleft()
            for neighbor in vertex.neighbors:
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    neighbor.previous = vertex
                    queue.append(neighbor)
                    if neighbor.label == end_label:
                        return self.get_path(end_label)
            vertex.color = 'black'
        return []

## Depth-First Search (DFS) with O(V + E) complexity, where V is the number of vertices and E is the number of edges.
    def dfs(self, start_label):
        for vertex in self.vertices.values():
            vertex.color = 'white'
            vertex.previous = None
        self.time = 0
        self.dfs_visit(self.vertices[start_label])

    def dfs_visit(self, vertex):
        vertex.color = 'gray'
        self.time += 1
        vertex.discovery_time = self.time
        for neighbor in vertex.neighbors:
            if neighbor.color == 'white':
                neighbor.previous = vertex
                self.dfs_visit(neighbor)
        vertex.color = 'black'
        self.time += 1
        vertex.closing_time = self.time

    def get_path(self, end_label):
        path = []
        step = self.vertices[end_label]
        while step.previous:
            path.append((step.previous.label, step.label))
            step = step.previous
        return path[::-1]

    def display_graph(self):
        for vertex in self.vertices:
            neighbors = [n.label for n in self.vertices[vertex].neighbors]
            print(f"{vertex}: {neighbors}")

# Example usage
if __name__ == "__main__":
    graph = AdjacencyList()
    if graph.read_graph("graph.txt"):
        print("Graph loaded successfully!")
        graph.display_graph()
        # Specify the vertices you want to search from and to
        start_vertex = 'a'
        end_vertex = 'p'
        path_bfs = graph.bfs(start_vertex, end_vertex)
        print(f"BFS path from {start_vertex} to {end_vertex}: {path_bfs}")
        graph.dfs(start_vertex)  # Start DFS from 'a'
        path_dfs = graph.get_path(end_vertex)
        print(f"DFS path from {start_vertex} to {end_vertex}: {path_dfs}")

        # Deleting a vertex and displaying graph again
        if graph.delete_vertex('E'):
            print("Vertex 'E' deleted.")
        else:
            print("Vertex 'E' not found.")
        graph.display_graph()
    else:
        print("Failed to load graph.")




