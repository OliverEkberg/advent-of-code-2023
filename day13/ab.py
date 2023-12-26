mirrors = [
  [[c for c in row] for row in chunk.splitlines()]
  for chunk in open('data.txt').read().split('\n\n')
]

def find_row_reflections(mirror):
  R = len(mirror)

  reflections = []

  for r in range(R-1):
    if mirror[r] != mirror[r+1]:
      continue

    r1 = r
    r2 = r+1

    while r1 >= 0 and r2 < R:
      if mirror[r1] != mirror[r2]:
        break
      r1-=1
      r2+=1
    else:
      reflections.append(r)
  
  return reflections

def find_reflections(mirror):
  row_reflections = [('row', reflection) for reflection in find_row_reflections(mirror)]
  col_reflections = [('col', reflection) for reflection in find_row_reflections(list(zip(*mirror[::-1])))]
  return row_reflections + col_reflections

def score(reflection):
  k = 100 if reflection[0] == 'row' else 1
  return k * (reflection[1] + 1)

def find_new_reflection(mirror):
  initial_reflection = find_reflections(mirror)[0]

  R = len(mirror)
  C = len(mirror[0])

  for r in range(R):
    for c in range(C):
      smudge = mirror[r][c]
      mirror[r][c] = '#' if smudge == '.' else '.'
      new_reflections = find_reflections(mirror)
      mirror[r][c] = smudge

      if initial_reflection in new_reflections:
        new_reflections.remove(initial_reflection)
        
      if new_reflections:
        new_reflection, = new_reflections
        return new_reflection

print(sum(map(score, (find_reflections(mirror)[0] for mirror in mirrors))))
print(sum(map(score, map(find_new_reflection, mirrors))))
