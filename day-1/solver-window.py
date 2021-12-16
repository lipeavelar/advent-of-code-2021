with open('input.txt') as f:
    lines = f.readlines()
    m = int(lines[0]) + int(lines[1]) + int(lines[2])
    count = 0
    for i in range(1, len(lines)-2):
        next_sum = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if m < next_sum:
            count += 1
        m = next_sum
    print (count)