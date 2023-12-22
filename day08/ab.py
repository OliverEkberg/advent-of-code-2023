from math import lcm

instructions, rows = open('data.txt').read().split('\n\n')

mapping = {}

for row in rows.splitlines():
  left, right = row.split(' = ')
  right = right[1:-1]
  mapping[left] = right.split(', ')

def steps(start, cond):
  i = 0
  curr = start
  while not cond(curr):
    ins = instructions[i % len(instructions)]
    curr = mapping[curr][0 if ins == 'L' else 1]
    i+=1

  return i

print(steps('AAA', lambda node: node == 'ZZZ'))
print(lcm(*(
  steps(start, lambda node: node[-1] == 'Z')
  for start 
  in mapping.keys()
  if start[-1] == 'A'
)))
