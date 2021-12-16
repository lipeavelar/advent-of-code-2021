with open('input.txt') as inp:
    f = 0
    d = 0
    a = 0
    for line in inp.readlines():
        command, value = line.split(' ')
        if command == 'forward':
            f += int(value)
            d += a * int(value)
        elif command == 'down':
            a += int(value)
        else:
            a -= int(value)
    print(f*d)
