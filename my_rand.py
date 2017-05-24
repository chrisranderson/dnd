import numpy as np
from scipy.stats import norm
randint = np.random.randint
draws = np.random.normal(50, 15, 100000)

def flip(p):  
  return np.random.rand() < p

def choose_from_list(l, n=1):
  if n == 1:
    return np.array(l)[randint(0, len(l), n)][0]
  else:
    return np.array(l)[randint(0, len(l), n)]

def percentile(count=1):
  draw = np.random.normal(50, 15, count).astype(int)
  return draw

def dc(bonus):
  count = 100000
  rolls = np.random.randint(1, 21, count) + bonus

  # success = roll >= potential_dc
  for potential_dc in range(1, 31):
    number_of_successes = len(rolls[rolls >= potential_dc])
    print('DC: {}, {}'.format(potential_dc, number_of_successes/count))

if __name__ == '__main__':
  dc(4)
