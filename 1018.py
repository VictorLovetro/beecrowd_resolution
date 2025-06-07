N = int(input())
lista = [100,50,20,10,5,2,1]
att = 0
for numero in lista:

    if numero == 100:
        nota_100  = N // 100
        att = N % 100

    elif numero == 50:
        nota_50 = att // 50
        att = att % 50
    
    elif numero == 20:
        nota_20 = att // 20
        att= att % 20

    elif numero == 10:
        nota_10 = att // 10
        att = att % 10

    elif numero == 5:
        nota_5 = att // 5
        att = att % 5
    
    elif numero == 2:
        nota_2 = att // 2
        att = att % 2
    
    elif numero == 1:
        nota_1 = att // 1
        att = att % 1

print(N)
print('{} nota(s) de R$ 100,00'.format(nota_100))
print('{} nota(s) de R$ 50,00'.format(nota_50))
print('{} nota(s) de R$ 20,00'.format(nota_20))
print('{} nota(s) de R$ 10,00'.format(nota_10))
print('{} nota(s) de R$ 5,00'.format(nota_5))
print('{} nota(s) de R$ 2,00'.format(nota_2))
print('{} nota(s) de R$ 1,00'.format(nota_1))
