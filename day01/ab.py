lines = [line.strip() for line in open('data.txt')]

digits = [str(n) for n in range(0, 10)]
spelled_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def calibration(line, digits, spelled_digits):
  found_digits = []

  for d in digits + spelled_digits:
    if d not in line:
      continue
    
    for idx, first in ((line.index(d), True), (line.rindex(d), False)):
      if idx != -1:
        found_digits.append((
          idx + (0 if first else len(d)), 
          str(spelled_digits.index(d)) if d in spelled_digits else d
        ))

  found_digits.sort()
  return int(found_digits[0][1] + found_digits[-1][1])

print(sum(calibration(line, digits, []) for line in lines))
print(sum(calibration(line, digits, spelled_digits) for line in lines))
