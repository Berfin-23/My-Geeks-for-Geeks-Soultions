## **Reverse Digits of a Number**

### **Problem**
You are given a number \( n \). Your task is to reverse the digits of the number \( n \) and return the reversed number.

### **Examples**
1. **Input:** \( n = 1234 \)  
   **Output:** 4321  
   Explanation: Reversing the digits of 1234 gives 4321.

2. **Input:** \( n = 1010 \)  
   **Output:** 101  
   Explanation: Reversing the digits of 1010 gives 101.

3. **Input:** \( n = 101 \)  
   **Output:** 101  
   Explanation: Reversing the digits of 101 gives 101 (the number remains the same).

---

### **Approach**
1. Initialize a variable `rev` to store the reversed number.
2. Use a `while` loop to extract digits from \( n \) one by one and build the reversed number.
3. Return the reversed number after the loop finishes.

---

### **Code Implementation**

```python
def reverseDigits(n):
    rev = 0  # Step 1: Initialize the reversed number to 0

    while n > 0:  # Step 2: Loop until all digits are processed
        digit = n % 10  # Step 3: Get the last digit of n
        n = n // 10  # Step 4: Remove the last digit from n
        
        rev = rev * 10 + digit  # Step 5: Append the digit to the reversed number

    return rev  # Step 6: Return the reversed number

# Example calls
print(reverseDigits(1234))  # Output: 4321
print(reverseDigits(1010))  # Output: 101
print(reverseDigits(101))   # Output: 101
```

---
## **Line-by-Line Explanation**

1. **`def reverseDigits(n):`**  
   This defines the function `reverseDigits`, which takes an integer \( n \) as an argument. The purpose of the function is to reverse the digits of the number \( n \).

2. **`rev = 0`**  
   Initializes a variable `rev` to store the reversed number. Initially, it is set to 0, as the reversed number starts as 0 and will be built digit by digit.

3. **`while n > 0:`**  
   Begins a `while` loop that will continue running as long as \( n \) is greater than 0. This loop is used to extract digits from \( n \) one by one and build the reversed number.

4. **`digit = n % 10`**  
   Extracts the last digit of \( n \) using the modulus operator (`%`). This operation gives the remainder when \( n \) is divided by 10, which is the last digit of \( n \).

5. **`n = n // 10`**  
   Removes the last digit of \( n \) by performing integer division (`//`). This effectively reduces \( n \) by one digit, allowing the next iteration to work with the remaining digits.

6. **`rev = rev * 10 + digit`**  
   Adds the extracted digit to the reversed number `rev`. First, the current `rev` is multiplied by 10 to shift its digits to the left, and then the new digit is added to the rightmost position. This builds the reversed number.

7. **`return rev`**  
   After the loop finishes (when \( n \) becomes 0), the function returns the reversed number stored in `rev`.
