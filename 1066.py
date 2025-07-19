positive_number = 0 
negative_number = 0
pair_number = 0
odd_number = 0

for laps in range(0,5):
    numbers = float(input())
    if numbers> 0:
        positive_number +=1

    if numbers < 0:
        negative_number += 1
    
    if numbers % 2 == 0:
        pair_number += 1
    
    if numbers % 2 != 0:
        odd_number +=1

print(f'{pair_number} valor(es) par(es)')
print(f'{odd_number} valor(es) impar(es)')
print(f'{positive_number} valor(es) positivo(s)')
print(f'{negative_number} valor(es) negativo(s)')