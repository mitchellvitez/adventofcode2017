pos = 0
skip_size = 0
l = [i for i in range(256)]

def round(i):
    global pos, skip_size, l

    for length in i:
        rs = list(reversed((l*2)[pos:pos+length]))

        for v, p in enumerate(range(pos, pos+length)):
            l[p % len(l)] = rs[v]

        pos += length + skip_size
        pos %= len(l)
        skip_size += 1

    return l

round1test = round([70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41])
assert round1test[0] * round1test[1] == 7888

def to_ascii(s):
    r = [ord(c) for c in s]
    return r + [17, 31, 73, 47, 23]

assert to_ascii('1,2,3') == [49,44,50,44,51,17,31,73,47,23]

def xorl(l):
    result = 0
    for x in l:
        result ^= x
    return result

assert xorl([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]) == 64

def reset():
    global pos, skip_size, l
    pos = 0
    skip_size = 0
    l = [i for i in range(256)]

def hash(s):
    reset()
    i = to_ascii(s)
    sparse = []
    for rnd in range(64):
        sparse = round(i)

    # print(sparse)

    dense = [xorl(sparse[i*16:(i+1)*16]) for i in range(16)]
    # print(dense)

    h = ''
    for dig in dense:
        h += ("%0.2x" % dig)

    return h

key = "ugkiagan"

grand_sum = 0
grid = []
for i in range(128):
    h = hash(f"{key}-{i}")
    b = [int(dig) for dig in list(bin(int(h, 16))[2:].zfill(128))]
    grid.append(b)
    grand_sum += sum(b)
print(grand_sum)

def print_grid():
    for row in grid:
        # print(row)
        for col in row:
            print('    |' if col is 0 else str(col).zfill(4)+'|', end="") 
        print()

def fill_neighbors(x, y, cur):
    global grid
    if x > 0 and grid[x-1][y] == 1:
        grid[x-1][y] = cur
        fill_neighbors(x-1, y, cur)
    if x < 127 and grid[x+1][y] == 1:
        grid[x+1][y] = cur
        fill_neighbors(x+1, y, cur)
    if y > 0 and grid[x][y-1] == 1:
        grid[x][y-1] = cur
        fill_neighbors(x, y-1, cur)
    if y < 127 and grid[x][y+1] == 1:
        grid[x][y+1] = cur
        fill_neighbors(x, y+1, cur)

def group(g):
    cur = 2
    for x, row in enumerate(g):
        for y, cell in enumerate(row):
            if cell == 1:
                g[x][y] = cur
                fill_neighbors(x, y, cur)
                cur += 1
    return g

import copy

import random
r = lambda: random.randint(0,255)
colors = {x: [r(), r(), r()] for x in range(9001)}
colors[0] = [0, 0, 0]
# img = [[colors[col for col in row] for row in g]]

# for row in g:
#     newrow = []
#     for col in row:
#         newrow.append(colors[col])
#     imagegrid.append(newrow)
# colors = {x: [255, 255, 255] for x in range(1071)}

def conways(g):
    g2 = [[0] * 128]*128
    for x, row in enumerate(g):
        for y, cell in enumerate(row):
            # get neighbors
            n = 0
            if x > 0 and y > 0 and x < 127 and y < 127:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i !=0 and j != 0:
                            if g[x+i][y+j] > 0:
                                n += 1

            if cell > 0 and n < 2:
                g2[x][y] = 0
            if cell > 0 and n == 2 or n == 3:
                g2[x][y] = 1
            if cell > 0 and n > 3:
                g2[x][y] = 0
            if cell == 0 and n == 3:
                g2[x][y] = 1
    return g2

import scipy.misc as smp
def main():
    g = grid
    g = group(g)
    imagegrid = []
    for row in g:
        newrow = []
        for col in row:
            newrow.append(colors[col])
        imagegrid.append(newrow)
    # img = smp.toimage(imagegrid)       # Create a PIL image
    # img.show()                      # View in default viewer
    # img.save('day14.png')
    # g = conways(g)

main()

# print_grid()
# print(cur - 2)

