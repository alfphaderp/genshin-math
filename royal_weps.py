from random import random

def simulate(base_crit_rate, refinement, n=1_000_000):
    """Simulate n hits of royal weapon given a base crit rate and refinement
    level. Returns the averaged crit rate of the simulation."""
    crit_count = 0
    stacks = 0
    for _ in range(n):
        if random() < base_crit_rate + stacks * (0.06 + 0.02 * refinement):
            crit_count += 1
            stacks = 0
        elif stacks < 5:
            stacks += 1
    return crit_count / n

def percentify(decimal):
    return str(round(decimal * 100, 2)) + '%'

def print_rate_table():
    """Prints the averaged crit rate for base crit rate from 0 to 100 and
    refinement level from 1 to 5."""
    print('\tR1\tR2\tR3\tR4\tR5')
    for i in range(0, 105, 5):
        print(i, end='\t')
        for j in range(1, 6):
            print(percentify(simulate(i / 100, j)), end='\t')
        print()
    print()

def print_delta_table():
    """Prints the averaged crit rate increase for base crit rate from 0 to 100
    and refinement level from 1 to 5."""
    print('\tR1\tR2\tR3\tR4\tR5')
    for i in range(0, 105, 5):
        print(i, end='\t')
        for j in range(1, 6):
            print('+' + percentify(simulate(i / 100, j) - i / 100), end='\t')
        print()
    print()

print_rate_table()
print_delta_table()
print("Conclusion: royal weapons are garbage.")