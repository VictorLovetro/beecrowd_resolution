a = 0 
g = 0 
d = 0
while True:
    menu = int(input())
    if menu == 1:
        a +=1
        
    elif menu == 2:
        g+=1
        
    elif menu == 3:
        d +=1
    
    elif menu == 4:
        print('MUITO OBRIGADO')
        break

print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')