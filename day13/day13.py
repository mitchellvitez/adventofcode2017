def caught(delay):
    global d
    for x in range(91):
        if x in d:
            if (x + delay - 1) % (d[x] * 2 - 2) == 0:
                return True
    return False

d = {}
with open('input.txt') as f:
    for line in f:
        depth, rnge = line.split(': ')
        d[int(depth)] = int(rnge)


for delay in range(10000000):
    if not caught(delay):
        print(delay - 1)
        break

    # wall = {}
    # sev = 0
    # for i in range(max(d) + 1):
    #     try:
    #         d[i]
    #         wall[i] = (delay - 1) % (d[i] * 2 - 2)
    #     except:
    #         wall[i] = None

        # # print(wall)
        # if wall[x] == 0:
        #     sev += x * d[x]
        #     # print(sev)
        #     return True
        # for s in wall:
        #     if wall[s] == None or d.get(s) is None:
        #         continue
        #     wall[s] = (wall[s] + 1) % (d[s] * 2 - 2)

# savedwalls = {}
# wall = {}
# for i in range(max(d) + 1):
#     try:
#         d[i]
#         wall[i] = 0
#     except:
#         wall[i] = None

# for b in range(10000000):
#     if b % 100000 == 0:
#         print('===', b)
#     for s in wall:
#         if wall[s] == None or d.get(s) is None:
#             continue
#         wall[s] = (wall[s] + 1) % (d[s] * 2)
#     savedwalls[b] = wall

def withdelay(delay):
    global savedwalls

    wall = savedwalls[delay]
    sev = 0
    caught = False

    for x in range(max(d) + 1):
        # print(wall)
        if wall[x] == 0:
            # print(x)
            caught = True
            break
            sev += x * d[x]
        for s in wall:
            if wall[s] == None or d.get(s) is None:
                continue
            wall[s] = (wall[s] + 1) % (d[s] * 2)

    # print(sev)
    if not caught:
        print(delay)
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
        input()
        return

# for delay in range(200000000):
#     if delay % 10000 == 0:
#         print('---', delay)
#     withdelay(delay)
