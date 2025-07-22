valores = input().split(' ')
x = int(valores[0])
y = int(valores [1])
z = int(valores [2])

lista = [x,y,z]
valor_crescente = sorted(lista)

for new_list in valor_crescente:
    print(new_list)
print()
for value in valores:
    print(value)