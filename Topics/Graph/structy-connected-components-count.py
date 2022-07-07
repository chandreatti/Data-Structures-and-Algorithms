stack = []
nodes_visited = []

def dft(graph):
  
  while stack != []:
    
    current_node = stack.pop()
    nodes_visited.append(current_node)
    
    for neighood in graph[current_node]:
      if neighood not in nodes_visited:
        stack.append(neighood)
  
  return True
  
def connected_components_count(graph):
  
  components_count = 0
  
  for node in graph:
    
    if node in nodes_visited:
      pass
    else:
      stack.append(node)
      components_count += dft(graph)
      
  return components_count
