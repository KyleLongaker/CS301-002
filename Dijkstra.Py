## Group Memebers: Katelyn Juhl, Kyle Longaker 

from pythonds3.graphs import PriorityQueue

def dijkstra(graph, start):
   pq = PriorityQueue()
   start.distance = 0
   pq.heapify([(v.distance, v) for v in graph])
   while pq:
      distance, current_v = pq.delete()
      for next_v in current_v.get_neighbors():
            new_distance = current_v.distance + current_v.get_neighbor(next_v)
            if new_distance < next_v.distance:
               next_v.distance = new_distance
               next_v.previous = current_v
               pq.change_priority(next_v, new_distance)

   def display_graph(self):
      """ Prints each vertex and its neighbors. """
      for vertex in self.vertices:
         neighbors = [n.label for n in self.vertices[vertex].neighbors]
         print(f"{vertex}: {neighbors}")















