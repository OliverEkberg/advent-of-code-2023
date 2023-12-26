from collections import defaultdict

steps = open('data.txt').read().strip().split(',')

def hash(step):
  value = 0
  for ch in step:
    value = ((value + ord(ch)) * 17) % 256
  return value

boxes = defaultdict(dict)

for step in steps:
  if '=' in step:
    label, value = step.split('=')
    # Here we take advantage of the nested dicts keeping insertion order
    boxes[hash(label)][label] = int(value)
  else:
    label = step.replace('-', '')
    boxes[hash(label)].pop(label, None)

print(sum(map(hash, steps)))
print(sum(
  (b+1) * (l+1) * lens
  for b, box in boxes.items()
  for l, lens in enumerate(box.values())
))
