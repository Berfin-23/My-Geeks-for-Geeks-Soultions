def is_armstrong(n):
    original_n = n
    sum = 0
    length = len(str(n))

    while n > 0:
        digit = n % 10
        n = n // 10
        sum = sum + digit ** length

    return sum == original_n

print(is_armstrong(153))  # True
print(is_armstrong(9474))  # True
print(is_armstrong(9475))  # False
