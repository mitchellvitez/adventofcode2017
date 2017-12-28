import copy

def max_bank(banks):
    m = 0
    index = 0
    for i, bank in enumerate(banks):
        if bank > m:
            m = bank
            index = i
    return index, m

banks = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
# banks = [0,2,7,0]
seen = []
iters = 0

while True:
    iters += 1
    i, blocks = max_bank(banks)
    # print(i, blocks)
    banks[i] = 0

    while blocks > 0:
        i = (i + 1) % len(banks)
        banks[i] += 1
        blocks -= 1

    if tuple(banks) in seen:
        print(iters)
        break

    seen.append(tuple(banks))

for i, l in enumerate(seen):
    if l == tuple(banks):
        print(iters-i-1)

