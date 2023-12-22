dp = dict()

def possible_arrangements(schema, groups):  
  key = (schema, groups)
  if key in dp:
    return dp[key]
  if len(schema) < (sum(groups) + len(groups) - 1):
    return 0

  if not groups:
    return 0 if '#' in schema else 1

  g = groups[0]
  arrangements = 0
  if schema[0] in '.?': 
    arrangements += possible_arrangements(schema[1:], groups)

  if '.' not in schema[:g]:
    if len(schema) == g:
      arrangements+=1
    elif len(schema) > g and schema[g] != '#':
      arrangements+= possible_arrangements(schema[(g+1):], groups[1:])        

  dp[key] = arrangements
  return arrangements

a = 0
b = 0
for row in open("data.txt").readlines():
  schema,groups = row.split()
  groups = tuple(int(x) for x in groups.split(','))

  a += possible_arrangements(schema, groups)
  dp.clear()
  b += possible_arrangements('?'.join([schema]*5), groups*5)
  dp.clear()

print(a)
print(b)
