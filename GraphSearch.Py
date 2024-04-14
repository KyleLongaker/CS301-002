## Group Memebers: Katelyn Juhl, Kyle Longaker 

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.color = "gray"
        self.time = self.time + 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        start_vertex.color = "black"
        self.time = self.time + 1
        start_vertex.closing_time = self.time

## Big (O) Running time: O(n) Because of the amaount of time it takes for the program to ecacuate though all of the nested for loops. 




# look at my code I added the two and fixed it and I also have the big O run time
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








