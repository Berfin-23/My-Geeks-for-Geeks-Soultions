def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

print(isPrime(-2)) # False
print(isPrime(23)) # True
print(isPrime(47)) # True
print(isPrime(15)) # False