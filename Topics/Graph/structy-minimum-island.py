
def valid_position(grid, nodes_visited, current_position):
  
  current_row, current_column = current_position
  
  number_rows = len(grid)
  number_columns = len(grid[0])

  range_rows = range(0, number_rows)
  range_columns = range(0, number_columns)

  if current_row not in range_rows:
    return False

  if current_column not in range_columns:
    return False

  if grid[current_row][current_column] == 'W':
    return False
  
  if current_position in nodes_visited:
    return False
  
  return True

def island_size(grid, nodes_visited, current_position):

  current_row, current_column = current_position

  if valid_position(grid, nodes_visited, current_position):
    nodes_visited.append(current_position)

    new_position_up = (current_row - 1, current_column)
    new_position_right = (current_row, current_column + 1)
    new_position_down = (current_row + 1, current_column)
    new_position_left = (current_row, current_column - 1)

    return True \
      + island_size(grid, nodes_visited, new_position_up) \
      + island_size(grid, nodes_visited, new_position_right) \
      + island_size(grid, nodes_visited, new_position_down) \
      + island_size(grid, nodes_visited, new_position_left)
  
  return False

def minimum_island(grid):
  
  nodes_visited = []
  minimum_island = float('inf')

  number_rows = len(grid)
  number_columns = len(grid[0])

  range_rows = range(0, number_rows)
  range_columns = range(0, number_columns)

  for row in range_rows:
    for column in range_columns:

      current_position = (row, column)

      if valid_position(grid, nodes_visited, current_position):
        size_island = island_size(grid, nodes_visited, current_position)
        
        if minimum_island > size_island:
            minimum_island = size_island
  
  return minimum_island
