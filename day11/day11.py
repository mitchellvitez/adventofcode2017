def count(instructions):
    # n = 0
    # s = 0
    # nw = 0
    # ne = 0
    # sw = 0
    # se = 0
    x = 0
    y = 0
    z = 0
    maxi = 0
    for i in instructions:
        i = i.replace('\n', '')
        if i == 'n':
            # n += 1
            x -= 1
            y += 1
        elif i == 's':
            # s += 1
            x += 1
            y -= 1
        elif i == 'nw':
            # nw += 1
            x -= 1
            z += 1
        elif i == 'se':
            # se += 1
            x += 1
            z -= 1
        elif i == 'sw':
            # sw += 1
            y -= 1
            z += 1
        elif i == 'ne':
            # ne += 1
            y += 1
            z -= 1
        else:
            print(i)
        dist = max(abs(x), abs(y), abs(z))
        if dist > maxi:
            maxi = dist

    # print('-')
    # print(n-s, ne-sw, nw-se)

    #  print(n, s, se, sw, ne, nw)
    #  print(x, y, z)

    #  print(max(x, y, z))
    #  print(max(abs(x), abs(y), abs(z)))

    # print(x, y, z)
    # return max(x, y, z)
    print(max(abs(x), abs(y), abs(z)))
    print(maxi)
    return max(abs(x), abs(y), abs(z))


    #  coords = (n - s, se - nw, sw - ne)
    #  print(coords)

#  print( count(['ne', 'ne', 'ne']) == 3)
#  print( count(['ne', 'ne', 'sw', 'sw']) == 0)
#  print( count(['ne', 'ne', 's', 's']) == 2)
#  print( count(['se', 'sw', 'se', 'sw', 'sw']) == 3)

# assert count(['ne', 'ne', 'ne']) == 3
# assert count(['ne', 'ne', 'sw', 'sw']) == 0
# assert count(['ne', 'ne', 's', 's']) == 2
# assert count(['se', 'sw', 'se', 'sw', 'sw']) == 3
# assert count(['n', 'n', 'n', 'n', 'ne', 'ne', 'ne', 'se', 'se']) == 7 
# assert count(['s', 's', 's', 's', 'se', 'se', 'se', 'ne', 'ne']) == 7 

maxi = 0
with open('input.txt') as f:
    instructions = f.read().split(',')
    count(instructions)

    # for i in range(len(instructions)):
        # dist = count(instructions[:i])
        # if dist > maxi:
            # maxi = dist
    # print(maxi)

