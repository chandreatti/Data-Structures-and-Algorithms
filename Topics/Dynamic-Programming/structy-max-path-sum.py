
def valid_position(grid, current_position):

  current_line, current_column = current_position

  lines = len(grid)
  columns = len(grid[0])

  range_lines = range(0, lines)
  range_columns = range(0, columns)

  if current_line not in range_lines:
    return False

  if current_column not in range_columns:
    return False
  
  return True

def is_destination(grid, current_position):

  lines = len(grid)
  columns = len(grid[0])

  destination = (lines - 1, columns - 1)

  if current_position == destination:
    return True
  else:
    return False

def max_path_sum(grid, current_position=(0,0), memo={}):

  current_line, current_column = current_position
  
  if not valid_position(grid, current_position):
    return 0
  
  if is_destination(grid, current_position):
    return grid[current_line][current_column]
  
  if current_position in memo:
    return memo[current_position]

  new_position_right = (current_line, current_column + 1)
  new_position_down = (current_line + 1, current_column)

  result_right = max_path_sum(grid, new_position_right, memo)
  result_down = max_path_sum(grid, new_position_down, memo)

  result = grid[current_line][current_column] + max(result_right, result_down)
  memo[current_position] = result
  
  return result
