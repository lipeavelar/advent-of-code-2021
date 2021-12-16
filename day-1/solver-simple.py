with open('input.txt') as f:
    lines = f.readlines()
    m = int(lines[0])
    count = 0
    for line in lines[1:len(lines)]:
        if m < int(line):
            count += 1
        m = int(line)
    print (count)