def test_list(current_list, current_bit, tie_breaker, prefix):
    if len(current_list) < 2:
        return current_list, prefix
    count = 0
    for number in current_list:
        if number[current_bit] == '1':
            count += 1
        else:
            count -= 1
    if count < 0:
        if tie_breaker == '1':
            tie_breaker = '0'
        else:
            tie_breaker = '1'
    prefix += tie_breaker
    return [[elem.strip() for elem in current_list if elem.startswith(prefix)], prefix]


with open('input.txt') as inp:
    lines = inp.readlines()
    o2_list, prefix_o2 = test_list(lines, 0, '1', '')
    co2_list, prefix_co2 = test_list(lines, 0, '0', '')
    for current_bit in range(1,12):
        o2_list, prefix_o2 = test_list(o2_list, current_bit, '1', prefix_o2)
        co2_list, prefix_co2 = test_list(co2_list, current_bit, '0', prefix_co2)
    print(int(o2_list[0],2)*int(co2_list[0],2))
