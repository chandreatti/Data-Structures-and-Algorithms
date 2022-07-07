from collections import deque

def has_path(graph, src, dst):
  
  queue = deque([src])
  
  while len(queue) > 0:
    
    current = queue.popleft()
    if current == dst:
      return True
    
    for neighood in graph[current]:
      queue.append(neighood)
      
  return False
