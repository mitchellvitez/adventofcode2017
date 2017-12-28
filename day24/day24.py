conns = []
with open('input.txt') as f:
    for line in f.read().splitlines():
        conns.append(tuple(map(int, line.split('/'))))

def flatsum(lst):
    s = 0
    for x in lst:
        s += x[0]
        s += x[1]
    return s

print(conns)

curr = (0, 0)
bridge = [curr]

maxbridge = [curr]
maxsum = 0

for conn in conns:
    if conn[0] == curr[1]:
        bridge.append(conn)
        curr = conn
    print(bridge)

