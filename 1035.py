valores=(input()).split(' ')
A = int(valores[0])
B = int(valores[1])
C = int(valores[2])
D = int(valores[3])

soma_CD = C + D
soma_AB = A + B


if B > C and D > A and soma_CD > soma_AB and A %2 ==0 and C> 0 and D> 0:
    print('Valores aceitos')

else:
    print('Valores nao aceitos')