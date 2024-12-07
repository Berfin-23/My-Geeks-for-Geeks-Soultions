# **Prime Number Function: Understanding and Explanation**

## **What is a Prime Number?**  
A prime number is a positive integer greater than 1 that has no divisors other than 1 and itself.  

### **Examples**  
- **Prime numbers**: \( 2, 3, 5, 7, 11, 13 \).  
- **Non-prime numbers**: \( 4, 6, 8, 9, 10 \) (divisible by numbers other than 1 and itself).  

---

## **Mathematical Approach to Check Primality**  
1. If \( n < 2 \), it is not prime.  
   - Any number less than 2 is not prime by definition.  
2. To check if \( n \) is prime:  
   - Test divisibility for numbers from \( 2 \) to \( \sqrt{n} \).  
   - If \( n \) is divisible by any of these numbers, it is **not prime**.  
   - If \( n \) is not divisible by any of these numbers, it is **prime**.  

### **Why Only Check Up to \( \sqrt{n} \)?**  
- Any divisor greater than \( \sqrt{n} \) will have a corresponding smaller divisor less than \( \sqrt{n} \).  
  For example, to check if \( 36 \) is prime:  
  - Divisors are: \( 2 \times 18, 3 \times 12, 6 \times 6 \).  
  - Beyond \( \sqrt{36} = 6 \), pairs repeat.  

---

## **Code for Primality Check**

```python
def isPrime(n):
    if n < 2:  # Numbers less than 2 are not prime
        return False
    
    for i in range(2, int(n ** 0.5) + 1):  # Check divisors up to √n
        if n % i == 0:  # If divisible, not prime
            return False
        
    return True  # If no divisors, it is prime

# Test Cases
print(isPrime(2))  # True
print(isPrime(3))  # True
print(isPrime(4))  # False
print(isPrime(15))  # False
```

---

## **Line-by-Line Explanation**

1. **`def isPrime(n):`**  
   - This defines a function named `isPrime` that takes a single parameter, \( n \), which is the number to check for primality.

2. **`if n < 2:`**  
   - This checks if \( n \) is less than 2.  
   - Numbers less than 2 are not prime, so the function immediately returns `False` for such inputs.

3. **`for i in range(2, int(n ** 0.5) + 1):`**  
   - This starts a `for` loop to iterate over integers \( i \) from \( 2 \) to \( \sqrt{n} \) (inclusive).  
   - \( \text{int}(n ** 0.5) \): Calculates the integer value of the square root of \( n \).  
   - Adding 1 ensures the loop includes \( \sqrt{n} \) if it's an integer.

4. **`if n % i == 0:`**  
   - Inside the loop, this checks if \( n \) is divisible by \( i \) (i.e., \( n \mod i = 0 \)).  
   - If \( n \) is divisible by \( i \), it means \( n \) is not a prime number, so the function returns `False`.

5. **`return True`**  
   - If the loop completes without finding any divisors, it means \( n \) is a prime number.  
   - The function then returns `True`.

6. **Test Cases**  
   - **`print(isPrime(2))`**  
     - \( n = 2 \): The function skips the loop because \( \sqrt{2} < 2 \), and directly returns `True` since 2 is prime.  
   - **`print(isPrime(3))`**  
     - \( n = 3 \): The loop doesn't find any divisors, so the function returns `True`.  
   - **`print(isPrime(4))`**  
     - \( n = 4 \): The loop detects that \( 4 \) is divisible by \( 2 \), so the function returns `False`.  
   - **`print(isPrime(15))`**  
     - \( n = 15 \): The loop detects that \( 15 \) is divisible by \( 3 \), so the function returns `False`.
