## **Find the Last Digit of \( a^b \)**

### **Problem**
You are given two numbers, \( a \) (the base) and \( b \) (the exponent). You need to find the last digit of \( a^b \) (the number formed by raising \( a \) to the power of \( b \)).

### **Examples**
1. **Input:** \( a = 3 \), \( b = 10)  
   **Output:** 9  
   Explanation: \( 3^{10} = 59049 \), and the last digit is 9.

2. **Input:** \( a = 6 \), \( b = 2 \)  
   **Output:** 6  
   Explanation: \( 6^2 = 36 \), and the last digit is 6.

---

### **Mathematical Insight**
The last digits of the powers of any integer \( a \) repeat in a cycle. For example:
- For \( a = 2 \), the last digits of the powers are \( 2, 4, 8, 6 \), repeating every 4 terms.
- For \( a = 3 \), the last digits of the powers are \( 3, 9, 7, 1 \), repeating every 4 terms.

### **Key Observations**
1. Only the last digit of \( a \) matters for finding the last digit of \( a^b \).
2. The position of \( b \) in the repeating cycle will give us the last digit of \( a^b \).

---

### **Steps**
1. Extract the last digit of \( a \).
2. If \( b = 0 \), return 1 (since any number raised to 0 equals 1).
3. Find the repeating cycle of last digits for the base \( a \).
4. Calculate \( b \mod \text{cycle length} \) to figure out where \( b \) falls in the cycle.
5. Return the corresponding last digit based on the modulus.

---

### **Simplified Code Explanation**

```python
def getLastDigit(a, b) -> int:
    # Extract the last digit of `a`
    last_digit = int(str(a)[-1])  
    
    # Convert `b` to a string (to handle large values of `b`)
    b = str(b)  
    
    # If `b` is 0, return 1 (since any number raised to 0 equals 1)
    if b == "0":
        return 1  
    
    # Generate the cycle of last digits
    cycle = []  
    current = last_digit
    while current not in cycle:
        cycle.append(current)  # Add current last digit to the cycle
        current = (current * last_digit) % 10  # Get the next last digit
    
    # Find the length of the repeating cycle
    length_of_cycle = len(cycle)  
    
    # Calculate the position of `b` in the cycle
    mod_b = 0
    for digit in b:
        mod_b = (mod_b * 10 + int(digit)) % length_of_cycle  
    
    # Determine the correct index in the cycle
    if mod_b != 0:
        index = mod_b - 1
    else:
        index = length_of_cycle - 1  
    
    # Return the corresponding last digit from the cycle
    return cycle[index]


# Example calls
print(getLastDigit(4, 1))  # Output: 4
print(getLastDigit(8, 91))  # Output: 2
