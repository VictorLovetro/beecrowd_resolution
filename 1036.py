def bahskara(A,B,C):
    from math import sqrt

    delta = B**2 - (4*A*C)

    if A == 0 or B ==0 or C ==0 or delta < 0:
        print("Impossivel calcular")
    
    else:
        x1 = (-B + sqrt(delta))/(2*A)
        print(f'R1 = {x1:.5f}')

        x1 = (-B - sqrt(delta))/(2*A)
        print(f'R2 = {x1:.5f}')

values = input().split(' ')
A = float(values[0])
B = float(values[1])
C = float(values[2])
bahskara(A,B,C)