
def min_change(amount, coins):
  response = _min_change(amount, coins, {})
  
  if response == float('inf'):
    return -1
  else:
    return response


def _min_change(amount, coins, memo):

  if amount == 0:
    return 0
  if amount < 0:
    return float('inf')
  if amount in memo:
    return memo[amount]
  
  min_coins = float('inf')
  for coin in coins:
    new_amount = amount - coin
    coins_possible_quantity = 1 + _min_change(new_amount, coins, memo)
    
    if coins_possible_quantity < min_coins:
      min_coins = coins_possible_quantity
  
  memo[amount] = min_coins
  return min_coins