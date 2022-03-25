digits = []
codes = []

with open("day8full.txt") as f:
  for line in f:
    d, c = line.split('|')
    digits.append( [''.join(sorted(x)) for x in d.strip().split()] )
    codes.append( [''.join(sorted(x)) for x in c.strip().split()] )

for d in digits:
  d.sort(key=lambda l: len(l))

print(digits)
print(codes)

def has_segment(input, segment):
  if len(segment & set(input)) == 2:
    return True
  return False

total = 0
for input, output in zip(digits, codes):
  code = {input[0]: 1, input[1]: 7, input[2]: 4, input[-1]: 8}
  cf = set(input[0])
  bd = set(input[2]) - cf
  for i in input[6:9]:
    if not has_segment(i, bd):
      code[i] = 0
    elif has_segment(i, cf):
      code[i] = 9
    else:
      code[i] = 6
  for i in input[3:6]:
    if has_segment(i, bd):
      code[i] = 5
    elif has_segment(i, cf):
      code[i] = 3
    else:
      code[i] = 2

  print(code)

  result = 0
  for i in range( len(output) ):
    base = pow(10, 3-i)
    result += base * code[ output[i] ]
  print(result)
  total += result

print(total)
