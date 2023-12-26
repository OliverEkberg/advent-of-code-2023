matrix = [[c for c in line.strip()] for line in open('data.txt')]
R = len(matrix)
C = len(matrix[0])

def expanded(matrix):
  return set(r for r, row in enumerate(matrix) if all(v == '.' for v in row))

expanded_rows = expanded(matrix)
expanded_cols = expanded(zip(*matrix[::-1]))

galaxies = [
  (r, c)
  for r, row in enumerate(matrix)
  for c, cell in enumerate(row)
  if cell == '#'
]

def sum_distances(scale):
  distances = {}

  for g1 in galaxies:
    for g2 in galaxies:
      key = tuple(sorted((g1, g2)))
      if g2 == g1 or key in distances:
        continue
      
      r_dist = sum(scale if idx in expanded_rows else 1 for idx in range(min(g1[0], g2[0]), max(g1[0], g2[0])))
      c_dist = sum(scale if idx in expanded_cols else 1 for idx in range(min(g1[1], g2[1]), max(g1[1], g2[1])))
      distances[key] = r_dist + c_dist

  return sum(distances.values())

print(sum_distances(2))
print(sum_distances(1000000))
