import string

program = []
with open('input.txt') as f:
    program = [line.replace('\n','') for line in f]

def setval(idx, val):
    global isp1
    if isp1: p1[idx] = val
    else: p2[idx] = val

# registers, pc, queue, waiting
p1 = [{'p': 0}, 0, [], False]
p2 = [{'p': 1}, 0, [], False]

def getval(args, idx):
    val = 0
    try: val = int(args[idx])
    except: val = registers[args[idx]]
    return val

isp1 = True
sentfrom1 = 0
pc = 0
while pc >= 0 and pc < len(program):
    registers, pc, queue, waiting = p1 if isp1 else p2
    cmd, *args = program[pc].split()
    if args[0] not in registers and args[0] in string.ascii_lowercase:
        registers[args[0]] = 0

    # print('p1' if isp1 else 'p2')
    # print(cmd, *args)
    # print(p1 if isp1 else p2)

    if cmd == 'snd':
        if isp1:
            p2[2].append(getval(args, 0))
        else:
            sentfrom1 += 1
            p1[2].append(getval(args, 0))
    elif cmd == 'set':
        registers[args[0]] = getval(args, 1)
    elif cmd == 'add':
        registers[args[0]] += getval(args, 1)
    elif cmd == 'mul':
        registers[args[0]] *= getval(args, 1)
    elif cmd == 'mod':
        registers[args[0]] %= getval(args, 1)
    elif cmd == 'rcv':
        if queue == []:
            pc -= 1
            setval(3, True)
        else:
            registers[args[0]], *queue = queue
            setval(3, False)
    elif cmd == 'jgz':
        val = getval(args, 0)
        if val > 0:
            pc += getval(args, 1) - 1
    else:
        print('unknown command')

    setval(0, registers)
    setval(1, pc + 1)
    setval(2, queue)

    # print(p1 if isp1 else p2)
    # input()

    isp1 = not isp1

    if p1[3] and p2[3]:
        import sys
        print(sentfrom1)
        sys.exit()

