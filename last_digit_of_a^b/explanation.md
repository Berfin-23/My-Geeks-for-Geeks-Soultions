# Find the Last Digit of \( a^b \)

## **Question**  
You are given two integer numbers, the base \( a \) and the index \( b \). You have to find the last digit of \( a^b \).  

### Examples  
- **Input**: \( a = 3 \), \( b = 10 \)  
  **Output**: 9  
  **Explanation**: \( 3^{10} = 59049 \). Last digit is 9.  

- **Input**: \( a = 6 \), \( b = 2 \)  
  **Output**: 6  
  **Explanation**: \( 6^2 = 36 \). Last digit is 6.  

---

## **General Mathematics**  
### Insight  
The last digits of the powers of any integer \( a \) form a **repeating cycle**.  
- For example:  
  - \( a = 2 \), last digits of powers: \( 2, 4, 8, 6 \) (cycle length = 4).  
  - \( a = 3 \), last digits of powers: \( 3, 9, 7, 1 \) (cycle length = 4).  
  - \( a = 7 \), last digits of powers: \( 7, 9, 3, 1 \) (cycle length = 4).  

### Observations
1. To find the last digit of \( a^b \), only the **last digit of \( a \)** matters.  
2. The position of \( b \) in the repeating cycle determines the last digit of \( a^b \).  

---

## **Algorithm**  

1. Extract the **last digit** of \( a \) since it determines the last digit of \( a^b \).  
2. If \( b = 0 \), return 1 (since \( a^0 = 1 \) for any \( a \)).  
3. Generate the **cycle of last digits** by repeatedly multiplying the last digit and recording the results until repetition begins.  
4. Compute \( b \mod \text{cycle length} \) to find \( b \)'s position in the cycle.  
5. If \( b \mod \text{cycle length} = 0 \), select the last element of the cycle. Otherwise, pick the corresponding element based on the modulus.  
6. Return the result.

---

## **Line-by-Line Code Explanation**

```python
def getLastDigit(a, b) -> int:
    # Extract the last digit of `a`
    last_digit = int(str(a)[-1])  
    
    # Convert `b` to a string (handles large numbers)
    b = str(b)  
    
    # If `b = 0`, return 1 (any number raised to power 0 is 1)
    if b == "0":
        return 1  
    
    # Generate the cycle of last digits
    cycle = []  
    current = last_digit
    while current not in cycle:
        cycle.append(current)  # Append current last digit to the cycle
        current = (current * last_digit) % 10  # Calculate the next last digit
    
    # Length of the repeating cycle
    length_of_cycle = len(cycle)  
    
    # Find `b % length_of_cycle` incrementally for large `b`
    mod_b = 0
    for digit in b:
        mod_b = (mod_b * 10 + int(digit)) % length_of_cycle  
    
    # Determine the index in the cycle
    if mod_b != 0:
        index = mod_b - 1
    else:
        index = length_of_cycle - 1  
    
    # Return the last digit from the cycle
    return cycle[index]


# Example calls
print(getLastDigit(4, 1))  # Output: 4
print(getLastDigit(8, 91))  # Output: 2
