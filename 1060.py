positive_numbers = 0
for laps in range(0,6):
    number = float(input())
    if  number > 0: 
        positive_numbers += 1
    
print(f'{positive_numbers} valores positivos')