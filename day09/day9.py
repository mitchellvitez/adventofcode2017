def cleanup(s):
    in_garbage = False
    ignore = False
    new_s = ''

    for char in s:
        if ignore:
            ignore = False
            continue

        if char == '<':
            in_garbage = True
        elif char == '!':
            ignore = True
        elif char == '>' and in_garbage:
            in_garbage = False

        if not in_garbage and char != '>' and char != ',':
            new_s += char

    return new_s

def garbage(s):
    in_garbage = False
    ignore = False
    total = 0

    for char in s:
        if ignore:
            ignore = False
            continue

        if in_garbage and char == '<':
            total += 1
        elif char == '<':
            in_garbage = True
        elif char == '!':
            ignore = True
        elif char == '>' and in_garbage:
            in_garbage = False
        elif in_garbage:
            total += 1

    return total

def score(s):
    s = cleanup(s)
    total = 0
    curval = 0
    for char in s:
        if char == '{':
            curval += 1
        elif char == '}':
            total += curval
            curval -= 1
    return total

assert score('{}') == 1
assert score('{{{}}}') == 6
assert score('{{},{}}') == 5
assert score('{{{},{},{{}}}}') == 16
assert score('{<a>,<a>,<a>,<a>}') == 1
assert score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
assert score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
assert score('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3

assert garbage('<>') == 0
assert garbage('<random characters>') == 17
assert garbage('<<<<>') == 3
assert garbage('<{!>}>') == 2
assert garbage('<!!>') == 0
assert garbage('<!!!>>') == 0
assert garbage('<{o"i!a,<{i<a>') == 10

with open('input.txt') as f:
    print(score(f.read()))
with open('input.txt') as f:
    print(garbage(f.read()))
