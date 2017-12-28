def sum_neighbors(x_, y_, grid):
    return sum([grid[a][b] for a in range(x_-1, x_+2) for b in range(y_-1, y_+2)]) - grid[x_][y_]

def display(grid):
    for row in grid:
        for col in row:
            print(col, end='\t')
        print()
    print()

grid = [[0 for i in range(1000)] for i in range(1000)]

basex = 500
basey = 500

def update(grid, x, y):
    s = sum_neighbors(basex+x, basey+y, grid)
    grid[basex+x][basey+y] = s
    if s > 361527:
        print(s)
        import sys
        sys.exit()
    return grid

x = 0
y = 0
grid[basex+x][basey+y] = 1
x = 1

for emu in range(1, 10):
    grid = update(grid, x, y)
    while y < emu:
        y += 1
        grid = update(grid, x, y)
    while x > -emu:
        x -= 1
        grid = update(grid, x, y)
    while y > -emu:
        y -= 1
        grid = update(grid, x, y)
    while x < emu+1:
        x += 1
        grid = update(grid, x, y)
    y += 1

