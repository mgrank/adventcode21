import graph, pprint
pprinter = pprint.PrettyPrinter()

def parseConnections(lines):
  connections = []
  for line in lines:
    b, e = line.strip().split('-')
    connections.append((b, e))
  return connections

with open("day12full.txt") as f:
  lines = f.readlines()

connections2 = parseConnections(lines)

connections = [ ('start', 'A'), ('start', 'b'), ('A', 'c'), ('A', 'b'), ('A', 'end'), ('b', 'd'), ('b', 'end') ]
connectionsS = [ ('start', 'b'), ('A', 'c'), ('A', 'b'), ('A', 'end'), ('b', 'end') ]
g = graph.Graph(connections2)
pprinter.pprint(g._graph)

pprinter.pprint( len(g.visitNeighbors('start')) )