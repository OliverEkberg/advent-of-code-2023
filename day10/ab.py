from sys import setrecursionlimit

setrecursionlimit(10**5)

matrix = [[c for c in line.strip()] for line in open('data.txt')]
R = len(matrix)
C = len(matrix[0])

# (from, to, delta)
moves = [
  (('S', '|', 'L', 'J'), ('|', '7', 'F'), (-1, 0)),
  (('S', '|', 'F', '7'), ('|', 'L', 'J'), (1, 0)),
  (('S', 'F', '-', 'L'), ('-', 'J', '7'), (0, 1)),
  (('S', 'J', '-', '7'), ('-', 'F', 'L'), (0, -1)),
]

start = next(
  (r, c) 
  for r, row in enumerate(matrix) 
  for c, cell in enumerate(row) 
  if cell == 'S'
)

max_distance = 0
visited = set()

def traverse_loop(node, distance):
  if node in visited:
    return
  visited.add(node)
  
  global max_distance
  max_distance = max(max_distance, distance)
  r, c = node

  for a, b, delta in moves:
    if matrix[r][c] in a:
      dr, dc = delta
      nr = r+dr
      nc = c+dc

      if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] in b:
        traverse_loop((nr,nc), distance+1)

traverse_loop(start, 0)
print((max_distance+1)//2)

inside = 0

for r, row in enumerate(matrix):
  for c, cell in enumerate(row):
    if (r, c) not in visited:
      matrix[r][c] = '.'

for sr, row in enumerate(matrix):
  for sc, cell in enumerate(row):
    if cell != '.':
      continue

    crosses = 0
    prev = None
    for cell in row[sc:]:
      if cell in '|':
        crosses+=1
      elif cell in 'LF':
        prev = cell
      elif (cell, prev) in {('7', 'L'),('J', 'F')}:
        crosses+=1
        prev = None

    if crosses % 2 == 1:
      inside+=1

print(inside)
