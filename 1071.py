primeiro_valor = int(input())
segundo_valor = int(input())
soma = 0
for valores in range(segundo_valor+1,primeiro_valor):
    if valores % 2 != 0:
        soma += valores
print(soma)

