from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**5)

matrix = [list(row.strip()) for row in open('data.txt')]
R = len(matrix)
C = len(matrix[0])

start = (0, 1)
end = (R-1, C-2)

directions = {
  '^': [[-1, 0]],
  '>': [[0, 1]],
  'v': [[1, 0]],
  '<': [[0, -1]],
  '.': [[-1, 0], [0, 1], [1, 0], [0, -1]],
}

def build_graph(start, consider_slopes):
  graph = defaultdict(dict)

  q = [start]
  while q:
    r,c = q.pop()

    for dr, dc in directions[matrix[r][c] if consider_slopes else '.']:
      nr = r+dr
      nc = c+dc
      if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] != '#':
        graph[(r,c)][(nr,nc)] = 1
        if (nr,nc) not in graph:
          q.append((nr,nc))
  return graph

def compress_graph(graph):
  removed = set()

  for node in graph:
    neighbours = graph[node]
    if len(neighbours) == 2:
      n1, n2 = neighbours

      if node not in graph[n1] or node not in graph[n2]:
        continue

      graph[n1][n2] = graph[n1][node] + graph[node][n2]
      del graph[n1][node]

      graph[n2][n1] = graph[n2][node] + graph[node][n1]
      del graph[n2][node]

      removed.add(node)
  
  for node in removed:
    del graph[node]
  
  return graph

def longest_path(start, end, graph):
  seen = set()

  def recurse(node, length):
    if node == end:
      return length
    
    if node in seen:
      return -1

    seen.add(node)

    longest_path = -1
    for neighbour in graph[node]:
      longest_path = max(longest_path, recurse(neighbour, length + graph[node][neighbour]))

    seen.remove(node)
    return longest_path

  return recurse(start, 0)

g1 = compress_graph(build_graph(start, True))
g2 = compress_graph(build_graph(start, False))

print(longest_path(start, end, g1))
print(longest_path(start, end, g2))
