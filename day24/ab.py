from z3 import Solver, Int

stones = [
  list(map(int, line.replace(' @', ',').split(', ')))
  for line in open('data.txt')
]

def a():
  least = 200000000000000
  most = 400000000000000

  def line_equation(stone):
    x, y, _, dx, dy, _ = stone
    x2 = x + dx
    y2 = y + dy

    k = (y2 - y) / (x2 - x)
    m = y - k * x

    return k, m
  
  def sign(num):
    if num == 0:
      return 0
    elif num > 0:
      return 1
    else:
      return -1

  def cross_inside_boundary(stone1, stone2):
    x1, _, _, dx1, _, _ = stone1
    x2, _, _, dx2, _, _ = stone2
    k1, m1 = line_equation(stone1)
    k2, m2 = line_equation(stone2)

    divisor = k2 - k1
    if divisor == 0:
      return False
    
    intersect_x = (m1 - m2) / divisor
    intersect_y = k1 * intersect_x + m1

    return (
      all(least <= v <= most for v in [intersect_x, intersect_y]) and
      all(sign(intersect_x - x) == sign(dx) for x, dx in [(x1, dx1), (x2, dx2)])
    )
  
  intersections = 0

  for i in range(len(stones)):
    for j in range(i+1, len(stones)):
      if cross_inside_boundary(stones[i], stones[j]):
        intersections+=1
  
  return intersections
  
def b():
  solver = Solver()

  x = Int('x')
  y = Int('y')
  z = Int('z')
  dx = Int('dx')
  dy = Int('dy')
  dz = Int('dz')

  for i, stone in enumerate(stones):
    stone_x, stone_y, stone_z, stone_dx, stone_dy, stone_dz = stone
    time = Int(i)
    solver.add(time > 0)
    solver.add(x + dx * time == stone_x + stone_dx * time)
    solver.add(y + dy * time == stone_y + stone_dy * time)
    solver.add(z + dz * time == stone_z + stone_dz * time)
  solver.check()

  return sum(solver.model()[v].as_long() for v in [x, y, z])

print(a())
print(b())
