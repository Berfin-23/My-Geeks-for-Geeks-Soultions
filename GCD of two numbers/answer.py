def gdc(a, b):
    while b != 0:
        a, b = b, a % b

    return a

print(gdc(10, 15))  # 5
print(gdc(14, 21))  # 7
print(gdc(3, 9))  # 3