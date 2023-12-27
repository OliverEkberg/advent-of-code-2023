from sys import setrecursionlimit

setrecursionlimit(10**5)

matrix = [line.strip() for line in open('data.txt')]
R = len(matrix)
C = len(matrix[0])

def calc_energized(r, c, dr, dc):
  memo = set()
  energized = set()

  def recurse(r, c, dr, dc):
    if r < 0 or r >= R or c < 0 or c >= C or (r,c,dr,dc) in memo:
      return
    
    memo.add((r,c,dr,dc))
    energized.add((r,c))

    cell = matrix[r][c]

    if cell == '.':
      recurse(r+dr,c+dc,dr,dc)
    elif cell == '|':
      if dr:
        recurse(r+dr,c+dc,dr,dc)
      else:
        recurse(r+1,c,1,0)
        recurse(r-1,c,-1,0)
    elif cell == '-':
      if dc:
        recurse(r+dr,c+dc,dr,dc)
      else:
        recurse(r,c+1,0,1)
        recurse(r,c-1,0,-1)
    elif cell == '/':
      recurse(r-dc,c-dr,-dc,-dr)
    elif cell == '\\':
      recurse(r+dc,c+dr,dc,dr)
  
  recurse(r,c,dr,dc)
  return len(energized)

print(calc_energized(0,0,0,1))
print(max(
  *[
    max(calc_energized(r,0,0,1), calc_energized(r,C-1,0,-1))
    for r in range(R)
  ],
  *[
    max(calc_energized(0,c,1,0), calc_energized(R-1,c,-1,0))
    for c in range(C)
  ]
))
