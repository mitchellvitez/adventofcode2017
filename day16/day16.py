d = set()
with open('input.txt') as f:
    l = list('abcdefghijklmnop')
    # l = list('abcde')

    
    # print(''.join(l))
    for i in range(16):
        # if i % 1000 == 0:
            # print(i)
        f.seek(0)
        for instr in f.read().split(','):
            if instr[0] == 's':
                num = int(instr[1:])
                l = l[-num:] + l[:-num]
            if instr[0] == 'x':
                a, b = instr[1:].split('/')
                l[int(a)], l[int(b)] = l[int(b)], l[int(a)]
            if instr[0] == 'p':
                p1, p2 = instr[1], instr[3]
                p1i, p2i = l.index(p1), l.index(p2)
                l[p1i], l[p2i] = p2, p1

        if ''.join(l) in d:
            print(i)
        d.add(''.join(l))

    print(''.join(l))

