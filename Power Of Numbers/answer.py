def reverse_exponentiation(n):
    reversed_number = 0
    original_n = n
    
    while n > 0:
        digit = n % 10
        n = n // 10
        
        reversed_number = reversed_number * 10 + digit
        
    return original_n ** reversed_number

print(reverse_exponentiation(10))
print(reverse_exponentiation(9))