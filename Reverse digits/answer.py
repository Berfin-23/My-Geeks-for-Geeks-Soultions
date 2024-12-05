def reverseDigits(n):
    rev = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        
        rev = rev * 10 + digit

    return rev

print(reverseDigits(1234))
print(reverseDigits(1010))
print(reverseDigits(101))