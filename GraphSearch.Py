## Group Memebers: Katelyn Juhl, Kyle Longaker 
from collections import deque

class Vertex:
   """
   A class representing a vertex in the graph.
   Attributes:
       label (str): The unique identifier for the vertex.
       color (str): Used for marking the vertex during searches (white, gray, black).
       previous (Vertex): Points to the previous vertex in a path (used for path reconstruction).
       discovery_time (int): Timestamp when the vertex was first discovered in DFS.
       closing_time (int): Timestamp when the vertex was fully processed in DFS.
       neighbors (set): A set of adjacent vertices (edges).
   """
   def __init__(self, label):
      self.label = label
      self.color = 'white'
      self.previous = None
      self.discovery_time = 0
      self.closing_time = 0
      self.neighbors = set()

   def __repr__(self):
      return 'Vertex({})'.format(self.label)


class AdjacencyList:
   """
   Graph represented by an adjacency list.
   Attributes:
       vertices (dict): A dictionary mapping labels to Vertex objects.
       time (int): Global timestamp used during DFS to set discovery and closing times.
   """
   def __init__(self):
      self.vertices = {}
      self.time = 0

   def add_vertex(self, label):
      """ Adds a vertex to the graph. Returns True if vertex was added, False if it already existed. """
      if label not in self.vertices:
         self.vertices[label] = Vertex(label)
         return True
      return False

   def add_edge(self, from_label, to_label):
      """ Adds an edge between two vertices. Returns True if both exist and edge was added, False otherwise. """
      if from_label in self.vertices and to_label in self.vertices:
         self.vertices[from_label].neighbors.add(self.vertices[to_label])
         self.vertices[to_label].neighbors.add(self.vertices[from_label])
         return True
      return False

   def delete_vertex(self, label):
      """ Removes a vertex and all its edges from the graph. Returns True if successful, False if vertex not found. """
      if label in self.vertices:
         for neighbor in list(self.vertices[label].neighbors):
            neighbor.neighbors.remove(self.vertices[label])
         del self.vertices[label]
         return True
      return False

   def delete_edge(self, from_label, to_label):
      """ Removes an edge between two vertices. Returns True if edge existed and was removed, False otherwise. """
      if from_label in self.vertices and to_label in self.vertices and \
        self.vertices[to_label] in self.vertices[from_label].neighbors:
         self.vertices[from_label].neighbors.remove(self.vertices[to_label])
         self.vertices[to_label].neighbors.remove(self.vertices[from_label])
         return True
      return False

   def read_graph(self, filepath):
      """ 
      Reads graph from a file and constructs the graph by adding vertices and edges.
      Returns True if file was read without errors, False otherwise.
      """
      try:
         with open(filepath, 'r') as file:
            file.readline()  # Skip the first line with counts
            vertices = file.readline().strip().split(',')
            for vertex in vertices:
               self.add_vertex(vertex.strip())
            for line in file:
               from_vertex, to_vertex = line.strip().split()
               self.add_edge(from_vertex, to_vertex)
         return True
      except IOError as e:
         print(f"File error: {e}")
         return False
      except ValueError as e:
         print(f"Value error: {e}")
         return False

   def dfs(self, start_label):
      """
      Performs a depth-first search starting from the specified vertex.
      Properly initializes all vertices to white before beginning.
      Returns None if the start vertex doesn't exist.
      """
      if start_label not in self.vertices:
         return None
      for vertex in self.vertices.values():
         vertex.color = 'white'
         vertex.previous = None
      self.time = 0
      self.dfs_visit(self.vertices[start_label])

   def dfs_visit(self, vertex):
      """ Helper function for DFS that visits vertices recursively. """
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

   def bfs(self, start_label, end_label):
      """
      Performs a breadth-first search from start_label to find end_label.
      Constructs the path from start to end if found. Returns the path as a list of edges or an empty list if no path.
      """
      if start_label not in self.vertices or end_label not in self.vertices:
         return None
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

   def get_path(self, end_label):
      """ Constructs the path from start to end vertex using the 'previous' pointers. """
      path = []
      step = self.vertices[end_label]
      while step.previous:
         path.append((step.previous.label, step.label))
         step = step.previous
      return path[::-1]

   def display_graph(self):
      """ Prints each vertex and its neighbors. """
      for vertex in self.vertices:
         neighbors = [n.label for n in self.vertices[vertex].neighbors]
         print(f"{vertex}: {neighbors}")

# Time Complexity:
# - Vertex addition: O(1)
# - Edge addition: O(1)
# - Vertex deletion: O(V)
# - Edge deletion: O(1)
# - DFS and BFS: O(V + E)
# - Path reconstruction: O(V)

# Example usage
if __name__ == "__main__":
   graph = AdjacencyList()
   if graph.read_graph('graph.txt'):
      print("Graph loaded successfully.")
      graph.display_graph()
   else:
      print("Failed to load graph.")

   print("DFS from 'a' to 'p':")
   path_dfs = graph.dfs('a')
   if path_dfs is not None:
      print(f"Path by DFS: {path_dfs}")
   else:
      print("DFS failed to start.")

   print("BFS from 'a' to 'p':")
   path_bfs = graph.bfs('a', 'p')
   if path_bfs is not None:
      print(f"Path by BFS: {path_bfs}")
   else:
      print("BFS failed to find a path.")


