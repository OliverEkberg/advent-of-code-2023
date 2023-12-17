a = 0
b = 0

hist = {}

for idx, row in enumerate([row.strip() for row in open('data.txt')]):
  factor = hist.get(idx, 1)
  b += factor

  w, h = row.split(': ')[1].split(' | ')
  w = [int(v) for v in w.split()]
  h = [int(v) for v in h.split()]

  matching = set(w) & set(h)
  
  if matching:
    a += 2 ** (len(matching) - 1)

  for offset in range(len(matching)):
    future_idx = idx + offset + 1
    hist[future_idx] = hist.get(future_idx, 1) + factor

  idx+=1

print(a)
print(b)
