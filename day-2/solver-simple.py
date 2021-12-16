with open('input.txt') as inp:
    f = 0
    d = 0
    for line in inp.readlines():
        command, value = line.split(' ')
        if command == 'forward':
            f += int(value)
        elif command == 'down':
            d += int(value)
        else:
            d -= int(value)
    print(f*d)
