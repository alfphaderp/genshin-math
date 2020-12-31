from functools import lru_cache
from collections import Counter
from random import random

import numpy as np

SOFT_PITY = 90

def simulate_5(rolls, until_pity=SOFT_PITY):
  """Simulates rolling ROLLS times, returns how many 5 stars you get."""
  count = 0
  while rolls > 0:
    if until_pity == 1 or random() < 0.006:
      count += 1
      until_pity = SOFT_PITY
    else:
      until_pity -= 1
    rolls -= 1
  return count

def distr_5(rolls, until_pity=SOFT_PITY, simulations=100000):
  """Probability distribution of 5 stars you get after rolling ROLLS times."""
  c = Counter()
  for _ in range(simulations):
    c[simulate_5(rolls, until_pity)] += 1
  for count in c.keys():
    c[count] /= simulations
  return c

def distr_conv(dists, simulations=100000):
  """Convolution of given probability distributions in DISTS"""
  c = Counter()
  choices = [np.random.choice(list(d.keys()), simulations, p=list(d.values())) for d in dists]
  for choice in zip(*choices):
    c[sum(choice)] += 1
  for count in c.keys():
    c[count] /= simulations
  return c

def report(distr, count):
  """Creates a report from a distribution DISTR and how many 5 stars you got COUNT"""
  print(f"{round(sum(p for e, p in distr.items() if e < count) * 100, 4)}% got fewer 5 stars than you.")
  print(f"{round(sum(p for e, p in distr.items() if e == count) * 100, 4)}% got as many 5 stars as you.")
  print(f"{round(sum(p for e, p in distr.items() if e > count) * 100, 2)}% got more 5 stars than you.")

# Example usage:
# You rolled 20 times on beginner banner, 100 times on character banner, 50 times on standard banner
# You got 2 5 star characters or weapons
# report(distr_conv([distr_5(20), distr_5(100), distr_5(50)]), 2)

# pulls = {"character": 72}
# report(distr_conv([distr_5(v) for v in pulls.values()]), 0)
# print()

print("Ryan's luck:")
pulls = {"beginner": 20, "character": 140, "standard": 72}
report(distr_conv([distr_5(v) for v in pulls.values()]), 2)
print()
print("Emma's luck:")
pulls = {"character": 141, "standard": 150}
report(distr_conv([distr_5(v) for v in pulls.values()]), 6)
print()
print("Howard's luck:")
pulls = {"beginner": 20, "character": 309, "weapon": 20, "standard": 151}
report(distr_conv([distr_5(v) for v in pulls.values()]), 5)
print()
print("Howard's luck (after getting his next pity):")
pulls = {"beginner": 20, "character": 309, "weapon": 20, "standard": 151}
report(distr_conv([distr_5(v) for v in pulls.values()]), 6)
print()
print("Catherine's luck:")
pulls = {"beginner": 20, "character": 169, "weapon": 20, "standard": 72}
report(distr_conv([distr_5(v) for v in pulls.values()]), 4)