rows = [row.strip() for row in open('data.txt')]
times, distances = [
  [int(num) for num in row.split() if num.isnumeric()]
  for row in rows
]

def compute(times, distances):
  ans = 1

  for time, distance in zip(times, distances):
    times_beaten = 0

    for t in range(time+1):
      time_left = time - t
      speed = t
      d = speed * time_left
      if d > distance:
        times_beaten += 1
    
    ans *= times_beaten

  return ans

print(compute(times, distances))
print(compute([int(''.join(map(str, times)))], [int(''.join(map(str, distances)))]))
