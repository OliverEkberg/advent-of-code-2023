from collections import Counter
from functools import cmp_to_key

lines = [
  (row.strip().split(' ')[0], int(row.strip().split(' ')[1]))
  for row in open('data.txt')
]

def score(hand, use_jokers):
  jokers = [c for c in hand if c == 'J'] if use_jokers else []
  non_jokers = [c for c in hand if c != 'J'] if use_jokers else [c for c in hand]

  card_group_sizes = sorted(Counter(non_jokers).values())

  if not card_group_sizes:
    card_group_sizes.append(len(jokers))
  else:
    # Always add jokers to largest group
    card_group_sizes[-1] += len(jokers)


  # This will make hands with larger groups dominate
  return -sum(cgs ** 2 for cgs in card_group_sizes)

def winnings(strength, use_jokers):
  def cmp(l1, l2):
    h1, _ = l1
    h2, _ = l2

    diff = score(h2, use_jokers) - score(h1, use_jokers)
    if diff:
      return diff
    
    for c1, c2 in zip(h1, h2):
      diff = strength.index(c2) - strength.index(c1)
      if diff:
        return diff
      
    return 0

  ranked_lines = sorted(lines, key=cmp_to_key(cmp))
  
  return sum(i * line[1] for i, line in enumerate(ranked_lines, 1))

print(winnings(['A','K','Q','J','T','9', '8', '7', '6', '5', '4', '3', '2'], False))
print(winnings(['A','K','Q','T','9', '8', '7', '6', '5', '4', '3', '2', 'J'], True))
