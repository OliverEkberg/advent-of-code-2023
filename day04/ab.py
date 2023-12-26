a = 0
b = 0

factors = {}

for idx, row in enumerate(open('data.txt')):
  factor = factors.get(idx, 1)
  b += factor

  num_matching = len(set.intersection(*[
    set(part.split())
    for part in row.split(': ')[1].split(' | ')]
  ))
  
  if num_matching:
    a += 2 ** (num_matching - 1)

  for offset in range(num_matching):
    future_idx = idx + offset + 1
    factors[future_idx] = factors.get(future_idx, 1) + factor

print(a)
print(b)
