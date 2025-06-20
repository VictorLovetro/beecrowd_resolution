nota = float(input())
lista_dinheiro = [100,50,20,10,5,2]
lista_moeda = [1,0.50,0.25,0.10,0.05,0.01]

resto = nota
print('NOTAS:')
for n in lista_dinheiro:
    quantidade = int(resto // n)
    print(f'{quantidade} nota(s) de R$ {n:.2f}')
    resto = round(resto % n, 2)

print('MOEDAS:')
for m in lista_moeda:
    quantidade = int(resto // m)
    print(f'{quantidade} moeda(s) de R$ {m:.2f}')
    resto = round(resto % m, 2)

