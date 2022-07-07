from collections import deque

queue = deque([])
visted_nodes = []

def largest_component(graph):
  
  largest = 0
  
  for node in graph:
    
    if node in visted_nodes:
      pass
    else:
      queue.append(node)
      component_size = bft(graph)
      if component_size > largest:
        largest = component_size
  
  return largest

def bft(graph):
  
  size = 0
  
  while queue:
    
    current = queue.popleft()
    if current not in visted_nodes:
      visted_nodes.append(current)
      size += 1
      for neighood in graph[current]:
        if neighood not in visted_nodes:
          queue.append(neighood)
  
  return size
