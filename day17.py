str = "target area: x=201..230, y=-99..-65"
test_str = "target area: x=20..30, y=-10..-5"

#str = test_str

xstr, ystr = str.split(':')[1].split(',')
xrange = [int(x) for x in xstr.split('=')[1].split('..')]
yrange = [int(y) for y in ystr.split('=')[1].split('..')]
print(xrange, yrange)

y_min = min(yrange)
v_down_max = abs(y_min)
y_vel = v_down_max - 1

def calcMaxHeight(vy):
  if vy <= 0:
    return 0
  max_h = 0
  while vy > 0:
    max_h += vy
    vy -= 1
  return max_h

print(calcMaxHeight(y_vel))