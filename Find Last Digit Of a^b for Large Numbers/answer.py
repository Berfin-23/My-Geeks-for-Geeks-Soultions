def getLastDigit(a, b) -> int:
    last_digit = int(str(a)[-1])
    b = str(b)
    
    if b == 0:
        return 1
    
    cycle = []
    current = last_digit
    while current not in cycle:
        cycle.append(current)
        current = (current * last_digit) % 10

    length_of_cycle = len(cycle)

    mod_b = 0

    for digit in b:
        mod_b = (mod_b * 10 + int(digit)) % length_of_cycle

    if mod_b != 0:
        index = mod_b - 1
    else:
        index = length_of_cycle - 1

    return cycle[index]


print(getLastDigit(4, 1))  # 4
print(getLastDigit(8, 91)) 
