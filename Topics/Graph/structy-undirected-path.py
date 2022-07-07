from collections import deque 

def makeGraph(edges):
  
  graph = {}
  
  for connection in edges:
    if (connection[0] not in graph):
      graph[connection[0]] = []
    if (connection[1] not in graph): 
      graph[connection[1]] = [] 
    
    graph[connection[0]].append(connection[1])
    graph[connection[1]].append(connection[0])
  
  return graph
    

def undirected_path(edges, node_A, node_B):
  
  graph = makeGraph(edges)
  queue = deque([node_A])
  nodes_visited = []
  
  while queue:
    
    current = queue.popleft()
    if current == node_B:
      return True
    
    nodes_visited.append(current)
    
    for node in graph[current]:
      if node not in nodes_visited:
        queue.append(node)
  
  return False
