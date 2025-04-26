value = input().split(' ')

a = float(value[0])
b = float(value[1])
c = float(value[2])

triangulo = a*c/2

circulo = 3.14159*c**2

trapezio = (a+b)*c/2

quadrado = b**2

retangulo = a*b

print(f'TRIANGULO: {triangulo:.3f}\n'
    f'CIRCULO: {circulo:.3f}\n'
    f'TRAPEZIO: {trapezio:.3f}\n'
    f'QUADRADO: {quadrado:.3f}\n'
    f'RETANGULO: {retangulo:.3f}')
