# def print_grid(g):
#     for row in g:
#         for cell in row:
#             print(cell, end='')
#         print()

grid = (('.','#','.'), ('.','.','#'), ('#','#','#'))

rules = {}

def flipx(grid):
    if len(grid) == 2:
        ((a,b),(c,d))= grid
        return ((b,a),(d,c))
    else:
        ((a,b,c),(d,e,f),(g,h,i))= grid
        return ((c,b,a),(f,e,d),(i,h,g))

def flipy(grid):
    if len(grid) == 2:
        ((a,b),(c,d))= grid
        return ((c,d),(a,b))
    else:
        ((a,b,c),(d,e,f),(g,h,i))= grid
        return ((g,h,i),(d,e,f),(a,b,c))

def flipdiag(grid):
    if len(grid) == 2:
        ((a,b),(c,d))= grid
        return ((d,b),(c,a))
    else:
        ((a,b,c),(d,e,f),(g,h,i))= grid
        return ((i,f,c),(h,e,b),(g,d,a))

def fixup(result):
    if len(result) != 4:
        return result
    else:
        ((a,b,c,d),(e,f,g,h),(i,j,k,l),(m,n,o,p)) = result
        return (((a,b),(e,f)),((c,d),(g,h)),((i,j),(m,n)),((k,l),(o,p)))

with open('input.txt') as f:
    for line in f:
        rule, result = line.replace('\n', '').split(' => ')
        rule = tuple([tuple(x) for x in rule.split('/')])
        result = tuple([tuple(x) for x in result.split('/')])

        result = fixup(result)
        # print(result)
        # input()
        rules[flipx(flipy(flipdiag(rule)))] = result
        rules[flipy(flipdiag(rule))] = result
        rules[flipx(flipdiag(rule))] = result
        rules[flipx(flipy(rule))] = result
        rules[flipdiag(rule)] = result
        rules[flipy(rule)] = result
        rules[flipx(rule)] = result
        rules[rule] = result

        # print(rules)
        # input()

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

def partial_flatten(container):
    for i in container:
        if type(i[0][0]) == type('.'):
            yield i
        else:
            for j in partial_flatten(i):
                yield j

def new_grid(g):
    if type(g[0][0]) == type('.'):
        return rules[g]
    return list(partial_flatten([new_grid(g2) for g2 in g]))

# import math
# def display(g):
#     size = int(math.sqrt(len(list(flatten(g)))))
#     # print(size)
#     i = 0
#     for x in range(size):
#         for y in range(size):
#             print(list(flatten(g))[i], end='')
#             i += 1
#         print()
#     print()

for iteration in range(19):
    # print_grid(grid)
    grid = new_grid(grid)
    # print(grid)
    # display(grid)
    # print(grid)
    # input()

# print('getting count')

print(sum([1 if c == '#' else 0 for c in flatten(grid)]) + 1)
