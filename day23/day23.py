a = 1
b = 107900
c = b + 17000
h = 0
while b - c:
    for d in range(2, b+1):
        if b % d == 0:
            if 2 <= b // d <= b:
                h += 1
                break
    b += 17
for d in range(2, b+1):
    if b % d == 0:
        if 2 <= b // d <= b:
            h += 1
            break
print(h)
