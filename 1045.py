valores = input().split()
lista_float = [float(x) for x in valores]
ordenada = sorted(lista_float, reverse = True)

a = ordenada[0]
b = ordenada[1]
c = ordenada[2]
if a >= b + c :
    print('NAO FORMA TRIANGULO')
    
else:
    if a **2 == b**2 + c **2 :
        print('TRIANGULO RETANGULO')

    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')

    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')

    if a== b and b== c and a==c:
        print('TRIANGULO EQUILATERO')

    elif a == b or a== c or b==c:
        print('TRIANGULO ISOSCELES')