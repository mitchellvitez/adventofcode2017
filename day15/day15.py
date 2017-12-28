a = 703
b = 516

total = 0

for i in range(5000000):
    a = (a * 16807) % 2147483647
    while (a % 4) != 0:
        a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while (b % 8) != 0:
        b = (b * 48271) % 2147483647

    if bin(a)[-16:] == bin(b)[-16:]:
        total += 1

print(total)
