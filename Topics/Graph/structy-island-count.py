
def valid_position(position, grid, spaces_visited):
  
  line, column = position
  
  number_rows = len(grid)
  number_columns = len(grid[0])
  
  range_of_rows = range(0, number_rows)
  range_of_columns = range(0, number_columns)
  
  if line not in range_of_rows:
    return False
  
  if column not in range_of_columns:
    return False
  
  if grid[line][column] == 'W':
    return False
  
  if position in spaces_visited:
    return False
  
  return True


def bfs(position, grid, spaces_visited):
  
  stack = [ position ]
  
  while stack != []:
  
    current_position = stack.pop()
    line, column = current_position
    spaces_visited.append(current_position)
    
    new_position_up = (line - 1, column)
    new_position_right = (line, column + 1)
    new_position_down = (line + 1, column)
    new_position_left = (line, column - 1)

    if valid_position(new_position_up, grid, spaces_visited):
      stack.append(new_position_up)

    if valid_position(new_position_right, grid, spaces_visited):
      stack.append(new_position_right)

    if valid_position(new_position_down, grid, spaces_visited):
      stack.append(new_position_down)

    if valid_position(new_position_left, grid, spaces_visited):
      stack.append(new_position_left)
  
  return True


def island_count(grid):
  
  spaces_visited = []
  number_of_islands = 0
  
  number_lines = len(grid)
  number_columns = len(grid[0])
  
  for line in range(number_lines):
    for column in range(number_columns):
      
      current_line = line
      current_column = column
      current_position = (current_line, current_column)
      
      if valid_position(current_position, grid, spaces_visited):
        number_of_islands += bfs(current_position, grid, spaces_visited)
  
  return number_of_islands
