## **Reverse Exponentiation**

### **Problem**  
Given a number \( n \), reverse its digits to form a new number \( r \) and compute \( n^r \) (the original number raised to the power of the reversed number).  

---

### **Examples**  

1. **Input:** \( n = 10 \)  
   **Output:** \( 10^1 = 10 \)  
   Explanation: Reversing \( 10 \) gives \( 01 \) (which is just 1). Therefore, \( 10^1 = 10 \).

2. **Input:** \( n = 9 \)  
   **Output:** \( 9^9 = 387420489 \)  
   Explanation: Reversing \( 9 \) gives \( 9 \). Thus, \( 9^9 = 387420489 \).

---

### **Approach**  

1. Reverse the digits of \( n \) to form the reversed number \( r \).  
2. Compute \( n^r \).  
3. Return the result.

---

### **Code Implementation**  

```python
def reverse_exponentiation(n):
    reversed_number = 0  # Step 1: Initialize reversed number to 0
    original_n = n       # Store the original number for final computation
    
    while n > 0:         # Step 2: Loop until all digits are processed
        digit = n % 10   # Extract the last digit of n
        n = n // 10      # Remove the last digit from n
        
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        
    return original_n ** reversed_number  # Step 3: Compute n^r and return the result

# Example calls
print(reverse_exponentiation(10))  # Output: 10
print(reverse_exponentiation(9))   # Output: 387420489

```
---

## **Line-by-Line Explanation**

1. **`def reverse_exponentiation(n):`**  
   This defines the function `reverse_exponentiation`, which takes an integer \( n \) as input. The function will reverse the digits of \( n \) and compute \( n^r \), where \( r \) is the reversed number.

2. **`reversed_number = 0`**  
   Initializes the variable `reversed_number` to store the reversed digits of \( n \). It starts at 0 and will be built digit by digit.

3. **`original_n = n`**  
   Stores the original value of \( n \) in the variable `original_n`. This is necessary because \( n \) will be modified (digits removed) in the loop, but the original value is needed for the final computation.

4. **`while n > 0:`**  
   Starts a `while` loop that continues until all digits of \( n \) are processed (i.e., \( n \) becomes 0). This loop is used to reverse the digits of \( n \).

5. **`digit = n % 10`**  
   Extracts the last digit of \( n \) using the modulus operator (`%`). This operation gives the remainder when \( n \) is divided by 10, which is the last digit.

6. **`n = n // 10`**  
   Removes the last digit of \( n \) by performing integer division (`//`). This reduces \( n \) to the remaining digits.

7. **`reversed_number = reversed_number * 10 + digit`**  
   Appends the extracted digit to `reversed_number`. This is done by multiplying the current `reversed_number` by 10 (shifting its digits to the left) and adding the extracted digit to the rightmost position.

8. **`return original_n ** reversed_number`**  
   After reversing the digits, the function calculates \( n^r \) using the `**` operator. \( original_n \) is raised to the power of `reversed_number` and returned as the result.
