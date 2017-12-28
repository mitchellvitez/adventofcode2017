program = []
with open('input.txt') as f:
    program = [line.replace('\n','') for line in f]

# print(program)

last_snd = 0
p2registers = {p: q}

pc = 0
while pc >= 0 and pc < len(program):
    # print(pc)
    # input()
    instr = program[pc].split()
    cmd, *args = instr
    if args[0] not in registers:
        registers[args[0]] = 0
    print(cmd, args)
    if cmd == 'snd':
        last_snd = registers[args[0]]
    elif cmd == 'set':
        try:
            registers[args[0]] = int(args[1])
        except:
            registers[args[0]] = registers[args[1]]
    elif cmd == 'add':
        registers[args[0]] += int(args[1])
    elif cmd == 'mul':
        registers[args[0]] *= int(args[1])
    elif cmd == 'mod':
        try:
            registers[args[0]] %= int(args[1])
        except:
            registers[args[0]] %= registers[args[1]]
    elif cmd == 'rcv':
        if registers[args[0]] != 0:
            import sys
            print(last_snd)
            sys.exit()
    elif cmd == 'jgz':
        if registers[args[0]] > 0:
            pc += int(args[1]) - 1
    else:
        print('unknown command')
        input()
    pc += 1

