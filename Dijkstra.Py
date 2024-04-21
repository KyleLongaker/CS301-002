## Group Memebers: Katelyn Juhl, Kyle Longaker 
import heapq

class PriorityQueue:
   def __init__(self):
      self.elements = []  
       # Underlying list for the priority queue

   def is_empty(self):
      # Check if the priority queue is empty
      # O(1) complexity
      return not self.elements

   def add(self, item, priority):
      # Add an item with its associated priority
      # O(log V) complexity, where V is the number of vertices in the queue
      heapq.heappush(self.elements, (priority, item))

   def delete(self):
      # Remove and return the item with the smallest priority
      # O(log V) complexity, where V is the number of vertices in the queue
      return heapq.heappop(self.elements)[1]


class Vertex:
   def __init__(self, label):
      self.label = label  
      # Identifier for the vertex
      self.neighbors = {}  
      # Stores neighbors and their edge weights
      self.distance = float('inf')  
      # Distance to this vertex from the source, default to infinity
      self.previous = None  
      # Previous vertex in optimal path traversal
      self.visited = False  
       # State to track if the vertex has been visited

   def __lt__(self, other):
      # Define comparison operation for priority queue based on distance
      # Helps the priority queue to compare vertices
      return self.distance < other.distance

   def add_neighbor(self, neighbor, weight=0):
      # Add a neighbor with the specified weight
      self.neighbors[neighbor] = weight

   def get_connections(self):
      # Return all vertices connected to this vertex
      return self.neighbors.keys()

   def get_weight(self, neighbor):
      # Get the weight to a connected vertex
      return self.neighbors[neighbor]


class WeightedAdjacencyList:
   def __init__(self):
      self.vert_dict = {}  
       # Stores vertices by label

   def __iter__(self):
      return iter(self.vert_dict.values())  
       # Allow iteration over vertices

   def add_vertex(self, node):
      # Create and return a new vertex
      new_vertex = Vertex(node)
      self.vert_dict[node] = new_vertex
      return new_vertex

   def add_edge(self, frm, to, cost=0):
      # Ensure both vertices exist in the graph and add an edge between them
      # Edge creation is O(1)
      if frm not in self.vert_dict:
         self.add_vertex(frm)
      if to not in self.vert_dict:
         self.add_vertex(to)
      self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

   def read_graph(self, filepath):
      # Read and build the graph from a file
      # Assumes that each line of the file represents an edge
      # File reading and graph construction generally O(E) where E is the number of edges
      try:
         with open(filepath, 'r') as file:
            for line in file:
               parts = line.split()
               if len(parts) != 3:
                  continue  
                   # Ignore lines that do not represent valid edges
               frm, to, cost = parts
               self.add_edge(frm, to, int(cost))
         return True
      except IOError as e:
         print(f"Error reading file: {e}")
         return False

def dijkstra(aGraph, start, target):
   # Dijkstra's algorithm to find the shortest path from start to target
   # O((V+E) log V) complexity, where V is the number of vertices and E is the number of edges
   start.distance = 0
   pq = PriorityQueue()
   pq.add(start)

   while not pq.is_empty():
      current = pq.delete()
      current.visited = True
      if current == target:
         break
   
      for next in current.get_connections():
         if next.visited:
            continue
         new_dist = current.distance + current.get_weight(next)
         if new_dist < next.distance:
            next.distance = new_dist
            next.previous = current
            pq.add(next)  # Reinsert with updated distance

   # Reconstruct the path from target to start by backtracking
   path = []
   step = target
   total_weight = target.distance
   while step.previous is not None:
      path.append((step.previous.label, step.label, step.get_weight(step)))
      step = step.previous
   path.reverse()  
   # Present the path from start to target

   return path, total_weight

if __name__ == '__main__':
   g = WeightedAdjacencyList()
   if g.read_graph('weightedGraph1.txt'):
      path, total_weight = dijkstra(g, g.get_vertex('a'), g.get_vertex('o'))
      print("Path:", path)
      print("Total weight:", total_weight)
   else:
      print("Failed to load graph.")
