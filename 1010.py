p1 = input().split(' ')
p2 = input().split(' ')

x_1 = float(p1[0])
y_1 = float(p1[1])
z_1 = float(p1[2])
x_2 = float(p2[0])
y_2 = float(p2[1])
z_2 = float(p2[2])

r = y_1 * z_1 + y_2 * z_2

print(f'VALOR A PAGAR: R$ {r:.2f}')

#compressed code

#p1 = list(map(float, input().split()))
#p2 = list(map(float, input().split()))
#r = p1[1] * p1[2] + p2[1] * p2[2]
#print(f'VALOR A PAGAR: R$ {r:.2f}')
