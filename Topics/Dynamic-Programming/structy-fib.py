
def fib(n, results = {}):
  
  if n < 0:
    return 0
  if n in [0, 1]:
    return n
  
  if n in results:
    return results[n]
  results[n] = fib(n - 1, results) + fib(n - 2, results)
  
  return results[n]
