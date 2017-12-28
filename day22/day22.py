def display(grid, pos):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            x, y = pos
            if x == i and y == j:
                print(cell, end=']')
            elif x == i and y-1 == j:
                print(cell, end='[')
            else:
                print(cell, end=' ')
        print()
    print()

size = 500
grid = [['.' for x in range(size)] for y in range(size)]
pos = (0,0)

with open('input.txt') as f:
    y = size // 2
    for line in f:
        row = list(line.replace('\n', ''))
        pos = (size // 2 + len(row) // 2, size // 2 + len(row) // 2) 
        for i, cell in enumerate(row):
            grid[y][size // 2 + i] = cell
        y += 1

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

direction = UP

def turn_left():
    global direction
    if direction == UP: direction = LEFT
    elif direction == LEFT: direction = DOWN
    elif direction == DOWN: direction = RIGHT
    elif direction == RIGHT: direction = UP

def turn_right():
    global direction
    if direction == UP: direction = RIGHT
    elif direction == LEFT: direction = UP
    elif direction == DOWN: direction = LEFT
    elif direction == RIGHT: direction = DOWN

def reverse():
    global direction
    if direction == UP: direction = DOWN
    elif direction == LEFT: direction = RIGHT
    elif direction == DOWN: direction = UP
    elif direction == RIGHT: direction = LEFT

count = 0
for i in range(10000000):
    # display(grid, pos)

    x, y = pos
    if grid[x][y] == '.':
        turn_left()
        grid[x][y] = 'W'
    elif grid[x][y] == '#':
        turn_right()
        grid[x][y] = 'F'
    elif grid[x][y] == 'W':
        count += 1
        grid[x][y] = '#'
    elif grid[x][y] == 'F':
        reverse()
        grid[x][y] = '.'

    dx, dy = direction
    pos = (x + dx, y + dy)

    # input()

# display(grid, pos)
print(count)
