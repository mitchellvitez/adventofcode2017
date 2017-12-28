program = []
with open('input.txt') as f:
    for line in f:
        program.append(int(line))

pc = 0
numSteps = 0

while pc > -1 and pc < len(program):
    numSteps += 1
    instr = program[pc]
    # if instr >= 3:
        # program[pc] = instr - 1
    # else:
    program[pc] = instr + 1
    pc += instr

print(numSteps)

# Part 2

program = []
with open('input.txt') as f:
    for line in f:
        program.append(int(line))
pc = 0
numSteps = 0
while pc > -1 and pc < len(program):
    numSteps += 1
    instr = program[pc]
    if instr >= 3:
        program[pc] = instr - 1
    else:
        program[pc] = instr + 1
    pc += instr
print(numSteps)

