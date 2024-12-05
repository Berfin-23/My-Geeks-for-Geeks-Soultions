def evenlyDivides(n):
        count = 0
        original_n = n
        
        while n > 0:
            digit = n % 10
            n = n // 10
            
            if (digit != 0) and (original_n % digit == 0):
                count += 1
                
        return count

print(evenlyDivides(1012))
print(evenlyDivides(1010))
print(evenlyDivides(101)) 
print(evenlyDivides(23)) 
