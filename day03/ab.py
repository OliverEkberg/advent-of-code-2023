from collections import defaultdict

matrix = [[c for c in line.strip()] for line in open('data.txt')]

delta = [1, 0, -1]

R = len(matrix)
C = len(matrix[0])

a = 0
b = 0

num_adj_stars = defaultdict(list)

for r in range(R):
  c = 0

  while c < C:
    adj_stars = set()
    num = ''
    is_adj = False

    char = matrix[r][c]

    while char.isdigit():
      num += char

      for dr in delta:
        for dc in delta:
          if dr == 0 and dc == 0:
            continue

          nr = r+dr
          nc = c+dc
          if 0 <= nr < R and 0 <= nc < C:
            adj_char = matrix[nr][nc]
            if adj_char != '.' and not adj_char.isdigit():
              is_adj = True
            if adj_char == '*':
              adj_stars.add((nr, nc))
      
      c+=1
      if c >= C:
        break
      char = matrix[r][c]

    if len(num):
      num = int(num)
      if is_adj:
        a += num

      for star in adj_stars:
        num_adj_stars[star].append(num)

    c+=1

for part_numbers in num_adj_stars.values():
  if len(part_numbers) == 2:
    b += part_numbers[0] * part_numbers[1]

print(a)
print(b)
