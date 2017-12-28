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

def hash(s):
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

def reset():
    global pos, skip_size, l
    pos = 0
    skip_size = 0
    l = [i for i in range(256)]

# reset()
# print(hash(''))
# reset()
# print(hash('AoC 2017'))
# reset()
# print(hash('1,2,3'))
# reset()
# print(hash('1,2,4'))
# reset()
print(hash('70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41'))

# import itertools
# from string import ascii_lowercase, ascii_uppercase

# seen = {}
# import random
# x = ascii_lowercase + ascii_uppercase + '0123456789'

# count = 0
# for r in range(0,110):
#     for s in itertools.product(x, repeat=r):
#         s = ''.join(s)
#         count += 1
#         if count % 100 == 0:
#             print(str(r) + ' ' + str(count) + ' ' + s)
#         # print(s)
#         reset()
#         h = hash(s)
#         if h in seen:
#             print("collision between {s} and {seen[h]} with hash {h}".format())
#             import sys
#             sys.exit()
#         seen[h] = s

