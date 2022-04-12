from collections import defaultdict
str = "target area: x=201..230, y=-99..-65"
test_str = "target area: x=20..30, y=-10..-5"

#str = test_str

xstr, ystr = str.split(':')[1].split(',')
xrange = [int(x) for x in xstr.split('=')[1].split('..')]
yrange = [int(y) for y in ystr.split('=')[1].split('..')]
print(xrange, yrange)

valid_ypos = defaultdict(list)
for start_vy in range(-100, 100):
  vy = start_vy
  y = 0
  for step in range(1,500):
    y += vy
    if y >= yrange[0] and y <= yrange[1]:
      valid_ypos[step].append( start_vy )
    vy -= 1

min_len = xrange[0]
min_vx = 0
x = 0
for min_vx in range(min_len//2):
  x += min_vx
  if x >= min_len:
    break

print(valid_ypos)
speed = set()
max_step = max(valid_ypos.keys())
for start_vx in range(min_vx, xrange[1]+1):
  vx = start_vx
  x = 0
  for step in range(1, max_step+1):
    x += vx
    if x >= xrange[0] and x <= xrange[1]:
      for start_vy in valid_ypos[step]:
        speed.add( (start_vx, start_vy) )
    if vx > 0:
      vx -= 1

#print(speed)
print(len(speed))