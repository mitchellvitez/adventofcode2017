import string

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3

def print_grid():
    global grid
    for line in grid:
        for char in line:
            print(char, end='')
        print()

def empty():
    global grid
    for line in grid:
        for char in line:
            if char != ' ':
                return False
    return True

grid = []
with open('input.txt') as f:
    grid = [list(line.replace('\n', '')) for line in f] 

path = ''
direction = DOWN
pos = (0, grid[0].index('|'))

steps = 0
while not empty():
    steps += 1
    # print(pos)
    # print_grid()
    # print(direction)
    # print(pos)
    # input()

    x, y = pos
    l = grid[x][y]

    if l in string.ascii_uppercase:
        path += l

    if direction == DOWN and x + 1 < len(grid) and l != '+':
        pos = (x+1, y)
    elif direction == UP and x - 1 >= 0 and l != '+':
        pos = (x-1, y)
    elif direction == RIGHT and y + 1 < len(grid[x]) - 1 and l != '+':
        pos = (x, y+1)
    elif direction == LEFT and y - 1 >= 0 and l != '+':
        pos = (x, y-1)
    else: 
        plus = True
        if x - 1 >= 0 and grid[x-1][y] != ' ':
            pos = (x - 1, y)
            direction = UP
        if y - 1 >= 0 and grid[x][y-1] != ' ':
            pos = (x, y - 1)
            direction = LEFT
        if x + 1 < len(grid) and grid[x+1][y] != ' ':
            pos = (x + 1, y)
            direction = DOWN
        if y + 1 < len(grid[0]) - 1 and grid[x][y+1] != ' ':
            pos = (x, y + 1)
            direction = RIGHT
    grid[x][y] = ' '

# print_grid()
print(path)
print(steps)
# assert path == "ABCDEF"

