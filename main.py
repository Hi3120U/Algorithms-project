import heapq


class Graph:

  def __init__(self, file_path):
    self.graph = self.read_graph_from_file(file_path)
    self.dest_nodes = ['H', 'K', 'Q', 'T']

  def dijkstra(self, start):
    distances = {node: float('inf') for node in self.graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
      current_distance, current_node = pq.pop(0)
      for neighbor, weight in self.graph[current_node]:
        distance = current_distance + weight
        if distance < distances[neighbor]:
          distances[neighbor] = distance
          pq.append((distance, neighbor))
          pq.sort()

    return distances

  def read_graph_from_file(self, file_path):
    graph = {}
    with open(file_path, 'r') as file:
      for line in file:
        source, dest, weight = line.strip().split()
        if source not in graph:
          graph[source] = []
        graph[source].append((dest, int(weight)))
    return graph

  def run_dijkstra_for_all_nodes(self):
    for start_node in self.graph.keys():
      distances = self.dijkstra(start_node)
      print(f"Shortest distances from node {start_node}:")
      for dest in self.dest_nodes:
        print(f"To {dest}: {distances[dest]}")


file_path = 'graph_data.txt'
graph = Graph(file_path)
graph.run_dijkstra_for_all_nodes()
