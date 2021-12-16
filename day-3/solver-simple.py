with open('input.txt') as inp:
    arr_count = [0]*12
    for line in inp.readlines():
        i = 0
        for char in line.strip():
            if char == '1':
                arr_count[i] += 1
            else:
                arr_count[i] -= 1
            i += 1
    e = ''
    g = ''
    for count in arr_count:
        if count < 0:
            g += '0'
            e += '1'
        else:
            g += '1'
            e += '0'
    print(int(g,2)*int(e,2))
