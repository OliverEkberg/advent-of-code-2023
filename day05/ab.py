seeds, *maps = open('data.txt').read().split('\n\n')

seeds = list(map(int, seeds.split(': ')[1].split()))

mappings = {}

for mapping in maps:
  key, *ranges = mapping.splitlines()
  src, _, dest = key.split()[0].split('-')

  mappings[src] = {
    'dest': dest,
    'ranges': [tuple(map(int, range.split())) for range in ranges]
  }

def valid(interval):
  return interval[0] < interval[1]

def apply(mappings, ranges):
  mapped = []
  iter = ranges

  for dest_start, src_start, length in mappings:
    src_end = src_start + length
    diff = dest_start - src_start

    next_iter = []
    for start, end in iter:
      left = [start, min(end, src_start)]
      middle = [max(start, src_start), min(end, src_end)]
      right = [max(src_end, start), end]

      if valid(left):
        next_iter.append(left)
      if valid(right):
        next_iter.append(right)
      if valid(middle):
        mapped.append([middle[0] + diff, middle[1] + diff])
    
    iter = next_iter

  return iter + mapped

def lowest(initial_ranges):
  low = float('inf')

  for range in initial_ranges:
    node = 'seed'
    ranges = [range]

    while node != 'location':
      mapping = mappings[node]
      ranges = apply(mapping['ranges'], ranges)
      node = mapping['dest']

    low = min(low, *(start for start, *_ in ranges))
  
  return low

print(lowest([[s, s+1] for s in seeds]))
print(lowest([[seeds[i], seeds[i] + seeds[i+1]] for i in range(0, len(seeds), 2)]))
