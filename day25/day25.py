state = 'A'
steps = 0
tape = [0 for i in range(100000)]
ptr = len(tape) // 2

for step in range(12861455):
    if state == 'A':
        if tape[ptr] == 0:
            tape[ptr] = 1
            ptr += 1
            state = 'B'
        elif tape[ptr] == 1:
            tape[ptr] = 0
            ptr -= 1
            state = 'B'

    elif state == 'B':
        if tape[ptr] == 0:
            tape[ptr] = 1
            ptr -= 1
            state = 'C'
        elif tape[ptr] == 1:
            tape[ptr] = 0
            ptr += 1
            state = 'E'

    elif state == 'C':
        if tape[ptr] == 0:
            tape[ptr] = 1
            ptr += 1
            state = 'E'
        elif tape[ptr] == 1:
            tape[ptr] = 0
            ptr -= 1
            state = 'D'

    elif state == 'D':
        if tape[ptr] == 0:
            tape[ptr] = 1
            ptr -= 1
            state = 'A'
        elif tape[ptr] == 1:
            tape[ptr] = 1
            ptr -= 1
            state = 'A'

    elif state == 'E':
        if tape[ptr] == 0:
            tape[ptr] = 0
            ptr += 1
            state = 'A'
        elif tape[ptr] == 1:
            tape[ptr] = 0
            ptr += 1
            state = 'F'

    elif state == 'F':
        if tape[ptr] == 0:
            tape[ptr] = 1
            ptr += 1
            state = 'E'
        elif tape[ptr] == 1:
            tape[ptr] = 1
            ptr += 1
            state = 'A'

print(sum(tape))
