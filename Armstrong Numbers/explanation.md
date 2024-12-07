# **Armstrong Number Function: Explanation**

## **What is an Armstrong Number?**

An **Armstrong number** (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.  

### **Examples:**
- **153** is an Armstrong number because:  
  \( 1^3 + 5^3 + 3^3 = 153 \)
  
- **9474** is an Armstrong number because:  
  \( 9^4 + 4^4 + 7^4 + 4^4 = 9474 \)

- **9475** is not an Armstrong number because:  
  \( 9^4 + 4^4 + 7^4 + 5^4 \neq 9475 \)

---

## **Code for Checking Armstrong Number**

```python
def is_armstrong(n):
    original_n = n  # Store the original number
    sum = 0  # Initialize a variable to hold the sum
    length = len(str(n))  # Calculate the number of digits in n

    while n > 0:  # Loop through each digit of the number
        digit = n % 10  # Extract the last digit
        n = n // 10  # Remove the last digit from n
        sum = sum + digit ** length  # Add the digit raised to the power of the number of digits

    return sum == original_n  # Check if the sum is equal to the original number

# Test Cases
print(is_armstrong(153))  # True
print(is_armstrong(9474))  # True
print(is_armstrong(9475))  # False
```

---

# Line-by-Line Explanation of Armstrong Number Function

1. **`def is_armstrong(n):`**  
   - This line defines the function `is_armstrong` which takes a single argument `n`, the number that we need to check for being an Armstrong number.

2. **`original_n = n`**  
   - The original value of \( n \) is stored in `original_n` because we will compare the sum of the digits raised to the power of the number of digits with this original number later.

3. **`sum = 0`**  
   - Initializes a variable `sum` to 0. This variable will be used to accumulate the sum of each digit raised to the power of the number of digits in \( n \).

4. **`length = len(str(n))`**  
   - Converts the number \( n \) to a string using `str(n)`, and then finds the length of that string using `len()`.  
   - The `length` represents the number of digits in \( n \).

5. **`while n > 0:`**  
   - Starts a `while` loop that runs as long as \( n \) is greater than 0 (i.e., until all digits of the number have been processed).

6. **`digit = n % 10`**  
   - Uses the modulo operation (`%`) to extract the last digit of \( n \).  
   - For example, if \( n = 153 \), then `digit = 153 % 10 = 3`.

7. **`n = n // 10`**  
   - Removes the last digit from \( n \) using integer division (`//`).  
   - For example, if \( n = 153 \), then `n = 153 // 10 = 15`.

8. **`sum = sum + digit ** length`**  
   - Raises the extracted digit (`digit`) to the power of the number of digits (`length`) and adds it to the `sum` variable.  
   - For example, if `digit = 3` and `length = 3`, then `sum = sum + 3^3 = sum + 27`.

9. **`return sum == original_n`**  
   - After the loop completes, this line compares the `sum` (the sum of the digits raised to the power of their count) with `original_n` (the original value of \( n \)).  
   - If the sum is equal to `original_n`, the function returns `True`, indicating that \( n \) is an Armstrong number. If not, it returns `False`.

10. **Test Cases**  
    - **`print(is_armstrong(153))`**: Returns `True` because 153 is an Armstrong number.  
    - **`print(is_armstrong(9474))`**: Returns `True` because 9474 is an Armstrong number.  
    - **`print(is_armstrong(9475))`**: Returns `False` because 9475 is not an Armstrong number.
