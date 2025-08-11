value = float(input())

cents = int(round(value*100))

notes = [10000,5000,2000,1000,500,200]
coins = [100,50,25,10,5,1]

print('NOTAS:')
for notice in notes:
    amount = cents // notice
    print(f'{amount} nota(s) de R$ {notice/100:.2f}')
    cents %=notice
    
print('MOEDAS:')
for coin in coins:
    amount=cents // coin
    print(f'{amount} moeda(s) de R$ {coin/100:.2f}')
    cents %= coin