program = []
with open('input.txt') as f:
    program = [line.replace('\n','') for line in f]

print(program)

registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f':0, 'g':0, 'h':0}

def getval(args, idx):
    val = 0
    try: val = int(args[idx])
    except: val = registers[args[idx]]
    return val

pc = 0
mulcount = 0
count = 0
while pc >= 0 and pc < len(program):
    if count % 1000000 == 0:
        print(registers)
        print(registers['h'])
        # input()
    instr = program[pc].split()
    cmd, *args = instr

    if cmd == 'set':
        registers[args[0]] = getval(args, 1)
    elif cmd == 'sub':
        registers[args[0]] -= getval(args, 1)
    elif cmd == 'mul':
        mulcount += 1
        registers[args[0]] *= getval(args, 1)
    elif cmd == 'jnz':
        val = getval(args, 0)
        if val != 0:
            pc += getval(args, 1) - 1

    pc += 1
    count += 1
# print(mulcount)
print(registers['h'])



