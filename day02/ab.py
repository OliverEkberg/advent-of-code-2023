from collections import defaultdict
from math import prod

constraints = {
  'red': 12,
  'green': 13,
  'blue': 14
}

a = 0
b = 0

for game in [line.strip() for line in open('data.txt')]:
  id, subsets = game.split(': ')
  id = int(id.split(' ')[1])

  subsets = [
    [r.split(' ') for r in subset.split(', ')] 
    for subset in subsets.split('; ')
  ]

  cubes = [
    (int(num), color)
    for subset
    in subsets
    for num, color
    in subset
  ]

  valid_game = all([
    (color in constraints and constraints[color] >= num)
    for num, color
    in cubes
  ])

  if valid_game:
    a += id

  max_per_color = defaultdict(int)

  for num, color in cubes:
    max_per_color[color] = max(max_per_color[color], num)

  b += prod(max_per_color.values())
  
print(a)
print(b)
