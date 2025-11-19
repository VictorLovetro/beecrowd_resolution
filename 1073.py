value = int(input())
valores = []
for values in range(value,0,-1):
    if values % 2 == 0:
        valores.append(values)
        ordenados = sorted(valores)
for n in ordenados:
    print(f'{n}^2 = {n ** 2}')