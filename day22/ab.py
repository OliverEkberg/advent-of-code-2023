lines = [
  [list(map(int, coord.split(','))) for coord in row.split('~')]
  for row in open('data.txt')
]

lines.sort(key=lambda coord: coord[0][2])

stopped = []

# Whether l2 is on top of l1
def touching(l1, l2):
  return max(l1[0][0], l2[0][0]) <= min(l1[1][0], l2[1][0]) and max(l1[0][1], l2[0][1]) <= min(l1[1][1], l2[1][1]) and (l1[1][2] - l2[0][2]) == -1

for i, line in enumerate(lines):
  while True:
    if line[0][2] == 1:
      stopped.append(line)
      break

    if any(touching(s, line) for s in stopped):
      stopped.append(line)
      break
    else:
      line[0][2]-=1
      line[1][2]-=1

supports = { i: [] for i in range(len(stopped)) }
is_supported_by = { i: [] for i in range(len(stopped)) }

for i, l1 in enumerate(stopped):
  for j, l2 in enumerate(stopped):
    if i == j:
      continue

    if touching(l1, l2):
      supports[i].append(j)
      is_supported_by[j].append(i)

a = sum(
  all(len(is_supported_by[s]) > 1 for s in supported) 
  for supported 
  in supports.values() 
)
print(a)

b = 0
for i in range(len(stopped)):
  fallen = set()
  layer = set([i])

  while len(layer):
    next_layer = set()

    for idx in layer:
      fallen.add(idx)
      for s in supports[idx]:
        if s in fallen:
          continue
        if all(v in fallen for v in is_supported_by[s]):
          next_layer.add(s)

    layer = next_layer

  b+=len(fallen)-1

print(b)
