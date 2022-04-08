from queue import PriorityQueue

map = []

with open("day15full.txt") as f:
  for line in f:
    map.append( [int(x) for x in line.strip() ] )

large_map =  [ [0] * len(map[0]) * 5 for _ in range(len(map) * 5) ]

for y in range(len(map)):
  for x in range(len(map[y])):
    for i in range(5):
      for j in range(5):
        new_risk = map[y][x] + i + j
        while new_risk > 9:
          new_risk -= 9
        large_map[y + len(map)*i][x + len(map[y])*j] = new_risk

#print(large_map)
map = large_map


start = (0,0)
end = ( len(map[0]) - 1, len(map) - 1 )

def heuristic(start, end):
  return abs(start[0] - end[0]) + abs(start[1] + end[1])

def neighbours(point):
  x, y = point
  ns = []
  if x > 0:
    ns += [(x-1, y)]
  if x < end[0]:
    ns += [(x+1, y)]
  if y > 0:
    ns += [(x, y-1)]
  if y < end[1]:
    ns += [(x, y+1)]
  return ns

def travelCostTo(point):
  return map[point[1]][point[0]]

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
  current = frontier.get()

  if current == end:
    break

  for next in neighbours(current):
    new_cost = cost_so_far[current] + travelCostTo(next)
    if next not in cost_so_far or cost_so_far[next] > new_cost:
      cost_so_far[next] = new_cost
      priority = cost_so_far[next] + heuristic(next, end)
      frontier.put(next, priority)
      came_from[next] = current

route = [end]
current = end
while current != start:
  prev = came_from[current]
  route.append( prev )
  current = prev
route.reverse()
print(route)
print(cost_so_far[end])

