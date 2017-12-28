d = {}

with open('input.txt') as f:
    for line in f:
        name = line.split()[0]
        weight = int(line.split('(')[1].split(')')[0])
        others = []
        try:
            others = line.split('-> ')[1].replace('\n','').split(', ')
        except:
            pass
        # if name == 'bhwnch':
        #     print(others)
        d[name] = (weight, others)

# print(d['qhyan'])
# print(d['fvifqfr'])
# print(d['rquaisv'])

def depth(x):
    if d[x][1] == [] or type(d[x][1]) == type(0):
        return 0
    else:
        depths = [depth(x) for x in d[x][1]]
        return max(depths) + 1

# mdepth = 1

def weights(x):
    # global mdepth
    if d[x][1] == []: #  or type(d[x][1]) == type(0):
        return d[x][0]
    else:
        ws = [weights(x) for x in d[x][1]]

        # print(ws)
        # if ws[1:] != ws[:-1]oio:
            # print("!!")
            # mdepth = depth(x)
        # if len(ws) > 6:
            # print(ws)
        # print(x)
        return d[x][0] + sum(ws)

def checksubs(x):
    if len(x) == 1 and type(x[0]) == type(1):
        return True
    if type(x) == type([[1]]) and type(x[0][0]) == type(1) and x[1:] != x[:-1]:
        print(x)
        # input()
        return False
    for l in x:
        return checksubs(l)

for k in d:
    weight = d[k][0]
    # print(k, d[k])
    d[k] = (weight, d[k][1], weights(k))
    # print(k, d[k])

for k in d:
    # d[k] = d[k][2]
    # checksubs(d[k])
    # print(k, d[k])
    if type(d[k][1]) == type([]) and len(d[k][1]) >= 1:
        y = d[d[k][1][0]][2]
        fail = False
        for x in d[k][1]:
            if d[x][2] != y:
                # print(y)
                # print(d[x])
                fail = True
        if fail:
            # print('--')
            # print(d[k][1])
            for x in d[k][1]:
                # print(d[x])
                pass

# print(d['ixoiuh'])
# print(d['jdxth'])
print(1464 - 6)

# for k in d:
#     weight = d[k][0]
#     d[k] = (weight, weights(k))

# maxi = ''
# maxim = 0
# for k in d:
#     if d[k][1] > maxim:
#         maxi = k
#         maxim = d[k][1]
# print(maxi)

