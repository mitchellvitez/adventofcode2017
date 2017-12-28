registers = {}

maxmaxi = 0

def check_cmpop(reg, cmpop, cmpamt):
    regval = int(registers[reg])
    if cmpop == '>': return regval > cmpamt
    if cmpop == '<': return regval < cmpamt
    if cmpop == '>=': return regval >= cmpamt
    if cmpop == '<=': return regval <= cmpamt
    if cmpop == '==': return regval == cmpamt
    if cmpop == '!=': return regval != cmpamt

with open('input.txt') as f:
    for line in f:
        reg = line.split()[0]
        reg2 = line.split()[4]
        registers[reg] = 0
        registers[reg2] = 0

with open('input.txt') as f:
    for line in f:
        reg, incdec, amt, _, regcmp, cmpop, cmpamt = line.split()
        amt, cmpamt = int(amt), int(cmpamt)
        if check_cmpop(regcmp, cmpop, cmpamt):
            if incdec == 'inc':
                registers[reg] += amt
            elif incdec == 'dec':
                registers[reg] -= amt
        if registers[reg] > maxmaxi:
            maxmaxi = registers[reg]
    # print(registers)

maxi = 0
for reg in registers:
    if registers[reg] > maxi:
        maxi = registers[reg]

print(maxi)
print(maxmaxi)

