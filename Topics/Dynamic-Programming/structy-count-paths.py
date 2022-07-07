
def valid_position(grid, current_position):

  lines = len(grid)
  columns = len(grid[0])

  current_line, current_column = current_position

  if current_line not in range(0, lines):
    return False

  if current_column not in range(0, columns):
    return False

  if grid[current_line][current_column] == 'X':
    return False

  return True

def is_destination(grid, current_position):

  current_line, current_column = current_position

  lines = len(grid)
  columns = len(grid[0])

  target_line = (lines - 1)
  target_column = (columns - 1)

  if (current_line == target_line) and (current_column == target_column):
    return True
  else:
    return False

def count_paths(grid, current_position=(0,0), memo={}):
  
  current_line, current_column = current_position
  
  # Position invalid
  if not valid_position(grid, current_position):
    return 0
  
  # Find destination
  if is_destination(grid, current_position):
    return 1
  
  # Repeated position
  if current_position in memo:
    return memo[current_position]

  new_right_position = (current_line, current_column + 1)
  new_down_position = (current_line + 1, current_column)

  result = count_paths(grid, new_right_position, memo) + count_paths(grid, new_down_position, memo)
  memo[current_position] = result
  return result
