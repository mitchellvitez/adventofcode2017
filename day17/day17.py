idx = 0
# buflen = 1
y = 0
for x in range(1, 50000001):
    idx += 337
    idx %= x
    idx += 1
    # idx = ((idx + 337) % x) + 1
    if idx == 1:
        y = x       
    # buflen += 1
    # if buf[1] not in ones:
        # ones.add(buf[1])
        # print(buf[1])

print(y)
# print(buf)
# print(buf[1])
# print(buf[buf.index(0) + 1])
