import math
import copy
import time
import cProfile

def time_function(func):
  def wrapper(self):
    start = time.perf_counter()
    func(self)
    end = time.perf_counter()
    print(func.__name__, start - end)
  return wrapper

def pow2sum(lvl):
  sum = 0
  while lvl > 0:
    lvl -= 1
    sum += pow(2, lvl)
  return sum

class FishNum:
  def __init__(self, num=None, parent=None, left=None, right=None):
    self.left, self.right = left, right
    self.num = num
    self.parent = parent
    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

  def isPair(self):
    return self.num == None

  def __add__(self, a):
    a1 = copy.deepcopy(self)
    a2 = copy.deepcopy(a)
    new_num = FishNum(left=a1,right=a2)
    return new_num

  def depth(self, cur_d = 0):
    if self.isPair():
      d1 = self.left.depth(cur_d + 1)
      d2 = self.right.depth(cur_d + 1)
      return max(d1, d2)
    else:
      return cur_d

  def partExists(self, lvl, part):
    if lvl == 0:
      return self
    bin_str = f'{part:0>{lvl}b}'
    cur_node = self
    for c in bin_str:
      if c == '0':
        if cur_node.left == None:
          return None
        cur_node = cur_node.left
      elif c == '1':
        if cur_node.right == None:
          return None
        cur_node = cur_node.right
    return cur_node

  def buildVisualString(self):
    if not self.isPair():
      return str(self.num)
    d = self.depth()
    lines = []
    for lvl in range(d+1):
      inv_lvl = d - lvl - 1
      parts_count = pow(2, lvl)
      string = ''
      for part in range( parts_count ):
        part_w = int(pow(2, inv_lvl) * 4)
        node_part = self.partExists(lvl, part)
        if node_part:
          start_x = pow2sum(inv_lvl)
          filled_width = pow(2, inv_lvl + 1) + 1
          if node_part.isPair():
            string += ' ' * (start_x) + '┌'
            string += '─' * ((filled_width - 2) // 2) + '┴' + '─' * ((filled_width - 2) // 2) + '┐'
            string += ' ' * (part_w - filled_width - start_x)
          else:
            num_str = str(node_part.num)
            string += ' ' * (part_w // 2 - len(num_str)) + num_str + ' ' * (part_w // 2)
        else:
          string += ' ' * part_w
      lines.append(string)
    return '\n'.join(lines)

  def __repr__(self):
    return self.buildVisualString()

  def magnitude(self):
    if not self.isPair():
      return self.num
    return 3 * self.left.magnitude() + 2 * self.right.magnitude()

  def explode(self):
    l = self.left.num
    r = self.right.num

    cur_node = self
    #ascending
    while cur_node.parent != None:
      if cur_node.parent.left != cur_node:
        cur_node = cur_node.parent.left
        break
      cur_node = cur_node.parent

    if cur_node.parent != None:
      #descending
      while cur_node.isPair():
        cur_node = cur_node.right
      cur_node.num += l

    cur_node = self
    #ascending
    while cur_node.parent != None:
      if cur_node.parent.right != cur_node:
        cur_node = cur_node.parent.right
        break
      cur_node = cur_node.parent

    if cur_node.parent != None:
      #descending
      while cur_node.isPair():
        cur_node = cur_node.left
      cur_node.num += r

    #replace node with 0
    self.left = None
    self.right = None
    self.num = 0

  def split(self):
    if self.isPair():
      raise Exception("Cant split, not a regular number")
    half = self.num / 2
    l, r = math.floor(half), math.ceil(half)
    self.left = FishNum(l, parent=self)
    self.right = FishNum(r, parent=self)
    self.num = None

  def process_explode(self, node, depth):
    if depth >= 4:
      if node.isPair():
        node.explode()
        return True
    return False

  def process_split(self, node, depth):
    if not node.isPair():
      if node.num >= 10:
        node.split()
        return True
    return False

  def traverse(self, process):
    stack = [(self, 0)]
    while len(stack) > 0:
      node_top, depth = stack.pop()
      if node_top.right:
        stack.append((node_top.right, depth+1))
      if node_top.left:
        stack.append((node_top.left, depth+1))
      if process(node_top, depth):
        return True
    return False

  def reduce(self):
    while True:
      if self.traverse(self.process_explode):
        continue
      if self.traverse(self.process_split):
        continue
      break

def fishnumFromStr(string):
  string = string.strip()
  root = FishNum()
  cur_node = root
  for c in string:
    if c=='[':
      pair_node = FishNum(parent=cur_node)
      cur_node.left = pair_node
      cur_node = pair_node
    if c==']':
      cur_node = cur_node.parent
    if c.isdigit():
      cur_node.num = int(c)
    if c==',':
      cur_node.parent.right = FishNum(parent=cur_node.parent)
      cur_node = cur_node.parent.right
  return root

a = FishNum(3)
b = FishNum(2)
c = FishNum(left=a, right=b)
d = FishNum(left=FishNum(4), right=c)
e = FishNum(left=FishNum(5), right=d)
f = FishNum(left=FishNum(6), right=e)
g = FishNum(left=f, right=FishNum(1))

def traverseAndPrint(fn):
  print("Before:")
  print(fn)
  fn.reduce()
  print("After:")
  print(fn)
  print()

a = fishnumFromStr("[[[[[9,8],1],2],3],4]")
b = fishnumFromStr("[[6,[5,[[3,2],4]]],1]")
c = a+b
#traverseAndPrint(c)

x = fishnumFromStr("[[[[4,3],4],4],[7,[[8,4],9]]]")
y = fishnumFromStr("[1,1]")
z = x + y
#traverseAndPrint(z)

with open("day18full.txt") as f:
  lines = f.readlines()

#part1
#n = fishnumFromStr(lines[0])
#for i in range(1, len(lines)):
#  n += fishnumFromStr(lines[i])
#  n.reduce()
#  #traverseAndPrint(n)
#print(n)
#print(n.magnitude())

#part2
magnitudes = []
numList = list(map(fishnumFromStr, lines))

for i in numList:
  for j in numList:
    if i != j:
      k = i + j
      k.reduce()
      magnitudes.append(k.magnitude())

print(max(magnitudes))
