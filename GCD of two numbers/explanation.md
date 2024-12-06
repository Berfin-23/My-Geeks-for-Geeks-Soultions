# **GCD Function: Understanding and Code Explanation**

## **What is GCD?**  
The Greatest Common Divisor (GCD) of two numbers \( a \) and \( b \) is the largest positive integer that divides both \( a \) and \( b \) without leaving a remainder.  

### **Example**  
1. \( \text{GCD}(10, 15) = 5 \)  
   Explanation: The divisors of 10 are \( \{1, 2, 5, 10\} \), and the divisors of 15 are \( \{1, 3, 5, 15\} \). The largest common divisor is \( 5 \).  

2. \( \text{GCD}(14, 21) = 7 \)  
   Explanation: The divisors of 14 are \( \{1, 2, 7, 14\} \), and the divisors of 21 are \( \{1, 3, 7, 21\} \). The largest common divisor is \( 7 \).  

---

## **How is GCD Found?**

The GCD can be calculated efficiently using the **Euclidean Algorithm**, which works as follows:  
1. If \( b = 0 \), then \( \text{GCD}(a, b) = a \).  
2. Otherwise, compute \( \text{GCD}(b, a \mod b) \), where \( a \mod b \) is the remainder when \( a \) is divided by \( b \).  
3. Repeat the process until \( b = 0 \).  

This method reduces the size of the numbers at each step, making it efficient even for large numbers.  

---

## **Code for GCD Using the Euclidean Algorithm**

```python
def gdc(a, b):
    while b != 0:
        a, b = b, a % b  # Swap `a` and `b`, compute the remainder
    
    return a  # When `b` becomes 0, `a` is the GCD
```
---

## **Line-by-Line Explanation**

1. **`def gdc(a, b):`**  
   - This defines a function named `gdc` that takes two integers \( a \) and \( b \) as inputs.  
   - The function will calculate and return the greatest common divisor (GCD) of these two numbers.

2. **`while b != 0:`**  
   - This starts a `while` loop that runs as long as \( b \neq 0 \).  
   - The loop is based on the Euclidean Algorithm, which reduces the problem size step by step.  

3. **`a, b = b, a % b`**  
   - This performs two operations in one step:  
     1. Assigns the value of \( b \) to \( a \).  
     2. Updates \( b \) to the remainder of \( a \div b \) (i.e., \( a \mod b \)).  
   - This effectively swaps \( a \) and \( b \), reducing the problem to finding the GCD of \( b \) and \( a \mod b \).

4. **`return a`**  
   - Once \( b = 0 \), the loop exits.  
   - At this point, \( a \) holds the greatest common divisor of the original inputs \( a \) and \( b \).  
   - The function returns this value.

5. **`print(gdc(10, 15))  # 5`**  
   - Calls the `gdc` function with \( a = 10 \) and \( b = 15 \).  
   - The GCD is calculated as \( 5 \) and printed.  

6. **`print(gdc(14, 21))  # 7`**  
   - Calls the `gdc` function with \( a = 14 \) and \( b = 21 \).  
   - The GCD is calculated as \( 7 \) and printed.  

7. **`print(gdc(3, 9))  # 3`**  
   - Calls the `gdc` function with \( a = 3 \) and \( b = 9 \).  
   - The GCD is calculated as \( 3 \) and printed.
