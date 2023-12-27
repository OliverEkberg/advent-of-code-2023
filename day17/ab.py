from heapq import heappush, heappop

matrix = [list(map(int, line.strip())) for line in open('data.txt')]
R = len(matrix)
C = len(matrix[0])

matrix[0][0] = 0

def dijkstra(min_consecutive, max_consecutive):
  distances = {}
  distances[(0,0,0,0,-1)] = 0

  pq = []
  heappush(pq, (-1, (0,0,0,0,-1)))

  while pq:
    _, start = heappop(pq)
    r,c,dr,dc,consecutive = start

    if r < 0 or r >= R or c < 0 or c >= C:
      continue

    neighbours = []

    if consecutive == -1:
      neighbours.append((r,c+1,0,1,1))
      neighbours.append((r,c-1,0,-1,1))
      neighbours.append((r+1,c,1,0,1))
      neighbours.append((r-1,c,-1,0,1))
    else:
      if consecutive < max_consecutive:
        neighbours.append((r+dr,c+dc,dr,dc,consecutive+1))
      if consecutive >= min_consecutive:
        if dr:
          neighbours.append((r,c+1,0,1,1))
          neighbours.append((r,c-1,0,-1,1))
        else:
          neighbours.append((r+1,c,1,0,1))
          neighbours.append((r-1,c,-1,0,1))
    
    for end in neighbours:
      if not end in distances:
        distances[end] = float('inf')
      
      if distances[end] > (distances[start] + matrix[r][c]):
        distances[end] = distances[start] + matrix[r][c]

        if r == (R-1) and c == (C-1):
          return distances[end]
        
        heappush(pq, (distances[end], end))
  
print(dijkstra(0, 3))
print(dijkstra(4, 10))
