from collections import deque

def makeGraph(edges):
  graph = {}
  
  for edge in edges:
    node_a, node_b = edge
    
    if node_a not in graph:
      graph[node_a] = []
    if node_b not in graph:
      graph[node_b] = []
    
    graph[node_a].append(node_b)
    graph[node_b].append(node_a)
  
  return graph


def shortest_path(edges, node_A, node_B):
  
  graph = makeGraph( edges )
  queue = deque([ (node_A, 0) ])
  nodes_visited = []
  
  while queue:
  
    current = queue.popleft()
    current_node, current_distance = current
    
    if current_node == node_B:
      return current_distance
    
    else:
      nodes_visited.append(current_node)
      for neighbor_node in graph[current_node]:
        if neighbor_node not in nodes_visited:
          queue.append((neighbor_node, current_distance + 1))
  
  return -1
