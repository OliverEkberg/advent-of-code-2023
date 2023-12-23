lines = [list(map(int, line.strip().split())) for line in open('data.txt')]

a = 0
b = 0

for line in lines:
  rows = [line]

  all_zero = False
  while not all_zero:
    all_zero = True
    prev_row = rows[-1]

    rows.append([
      prev_row[i+1]-prev_row[i]
      for i in range(len(prev_row) - 1)
    ])
    all_zero = all(v == 0 for v in rows[-1])
  
  for i, row in reversed(list(enumerate(rows))):
    row.append((0 if i+1 >= len(rows) else rows[i+1][-1]) + row[-1])
    row.insert(0, row[0] - (0 if i+1 >= len(rows) else rows[i+1][0]))
  
  a += rows[0][-1]
  b += rows[0][0]

print(a)
print(b)
