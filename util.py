
def repeat(function, n):
  return [function() for _ in range(n)]

def repeat_format(function, n):
  return ', '.join(repeat(function, n))
