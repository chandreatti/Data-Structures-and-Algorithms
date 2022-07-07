
def sum_possible(amount, numbers, memo={}):

  if amount == 0:
    return True
  if amount < 0:
    return False
  if amount in memo:
    return memo[amount]

  for number in numbers:
    
    remaining = amount - number
    result = sum_possible(remaining, numbers)
    if result:
      memo[amount] = True
      return True
  
  memo[amount] = False
  return False