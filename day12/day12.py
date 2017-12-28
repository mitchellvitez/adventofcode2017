graph = {}
with open('input.txt') as f:
    for line in f:
        first, rest = line.split(' <-> ')
        first = int(first)
        if first not in graph:
            graph[first] = set()
        for x in rest.split(', '):
            graph[first].add(int(x))

# print(graph)

fullgraph = set()
fullgraph.add(0)

def build(start):
    global fullgraph
    for x in graph[start]:
        if x not in fullgraph:
            fullgraph.add(x)
            build(x)

build(0)
# print(fullgraph)
print(len(fullgraph))

fullgraphs = set()
for i in range(2000):
    fullgraph = set()
    fullgraph.add(i)
    build(i)
    if fullgraph not in fullgraphs:
        fullgraphs.add(tuple(sorted(list(fullgraph))))

print(len(fullgraphs))
