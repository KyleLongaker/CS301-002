## Group Memebers: Katelyn Juhl, Kyle Longaker 
from pythonds3.graphs import PriorityQueue

class Vertex: 
    def __init__(self, label):
        self.label = label
        self.neighbors = {}
        self.distance = float('inf')
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class WeightedAdjacencyList:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def read_graph(self, filepath):
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    parts = line.split()
                    if len(parts) != 3:
                        continue  # Not a valid edge definition
                    frm, to, cost = parts
                    self.add_edge(frm, to, int(cost))
            return True
        except IOError as e:
            print(f"Error reading file: {e}")
            return False

## Big O Running Time: O(log (n)) because of the while loop and how long it take to run the code. 

def dijkstra(aGraph, start, target):
    print('''Dijkstra's shortest path''')
    # Set the distance for the start node to zero 
    start.distance = 0

    # Put tuple pair into the priority queue
    unvisited_queue = PriorityQueue()
    unvisited_queue.add(start)

    while not unvisited_queue.is_empty():
        # Pops a vertex with the smallest distance 
        current = unvisited_queue.delete()

        # for next in v.adjacent:
        for next in current.get_connections():
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_weight(next) + current.distance

            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_vertex_id(), next.get_vertex_id(), next.distance))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_vertex_id(), next.get_vertex_id(), next.distance))

        while unvisited_queue:
            heapq.heappop(unvisited_queue)

        # Rebuild heap
        # 1. Pop every item
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.distance, v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

if __name__ == '__main__':
    g = WeightedAdjacencyList()
    g.read_graph('weightedGraph1.txt')
    dijkstra(g, g.get_vertex('a'), g.get_vertex('o'))  # provide the start and end vertices










