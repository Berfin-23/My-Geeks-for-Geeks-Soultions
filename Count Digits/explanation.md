## **Count Digits that Divide the Number**

### **Problem**

You are given a number \( n \). Your task is to count how many digits in \( n \) evenly divide the number \( n \).

### **Examples**

1. **Input:** \( n = 1012 \)  
   **Output:** 3  
   Explanation: Digits 1, 1, and 2 divide 1012 evenly.

2. **Input:** \( n = 1010 \)  
   **Output:** 2  
   Explanation: Digits 1 and 1 divide 1010 evenly.

3. **Input:** \( n = 101 \)  
   **Output:** 2  
   Explanation: Digits 1 and 1 divide 101 evenly.

4. **Input:** \( n = 23 \)  
   **Output:** 1  
   Explanation: Only the digit 2 divides 23 evenly.

---

### **Approach**

1. Convert the number \( n \) into its digits.
2. Check if each digit divides \( n \) without leaving a remainder.
3. Count how many digits divide \( n \) evenly.

---

### **Code Implementation**

```python
def evenlyDivides(n):
    # Step 1: Initialize a variable to count the number of digits that divide n evenly
    count = 0

    # Step 2: Save the original value of n to use it later for modulus checks
    original_n = n

    # Step 3: Use a while loop to go through each digit of the number n
    while n > 0:
        # Step 4: Get the last digit of n
        digit = n % 10

        # Step 5: Remove the last digit from n
        n = n // 10

        # Step 6: Check if the digit is not zero and divides original_n evenly
        if (digit != 0) and (original_n % digit == 0):
            # If the condition is true, increase the count
            count += 1

    # Step 7: Return the count of digits that divide n evenly
    return count

# Example calls
print(evenlyDivides(1012))  # Output: 3
print(evenlyDivides(1010))  # Output: 2
print(evenlyDivides(101))   # Output: 2
print(evenlyDivides(23))    # Output: 1
```

---

## **Line-by-Line Explanation**

1. **`def evenlyDivides(n):`** 
   This defines the function `evenlyDivides`, which takes an integer \( n \) as input. The function will calculate how many digits in \( n \) divide \( n \) evenly.

2. **`count = 0`**  
   This initializes a variable `count` to 0. It will keep track of how many digits divide \( n \) evenly.

3. **`original_n = n`**  
   This stores the original value of \( n \) in a new variable called `original_n`. We need this because we will modify \( n \) while extracting its digits, and we want to compare the digits to the original number.

4. **`while n > 0:`**  
   This starts a `while` loop that will continue as long as \( n \) is greater than 0. The loop will process each digit of \( n \) one by one.

5. **`digit = n % 10`**  
   The expression `n % 10` calculates the last digit of \( n \). This works by getting the remainder when \( n \) is divided by 10. For example, if \( n = 1012 \), this will give the digit 2 (the last digit).

6. **`n = n // 10`**  
   The expression `n // 10` removes the last digit from \( n \) by performing an integer division of \( n \) by 10. For example, if \( n = 1012 \), after this operation, \( n \) becomes 101.

7. **`if (digit != 0) and (original_n % digit == 0):`**  
   This condition checks two things:
   - The first part `(digit != 0)` ensures that we don't divide by zero, as dividing by zero would cause an error.
   - The second part `(original_n % digit == 0)` checks if the digit divides the original number \( n \) evenly. If the remainder when dividing \( n \) by the digit is 0, then the digit divides \( n \) evenly.

8. **`count += 1`**  
   If the above condition is true, it means the digit divides \( n \) evenly. We increase the `count` by 1 to keep track of how many digits divide \( n \) evenly.

9. **`return count`**  
   After processing all the digits of \( n \), the function returns the final count of digits that divide \( n \) evenly.

