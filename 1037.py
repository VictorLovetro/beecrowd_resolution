valor_tempo = float(input())

if 0 <= valor_tempo <= 25.00:
    print('Intervalo [0,25]')

elif 25.00 < valor_tempo <= 50.00:
    print('Intervalo (25,50]')

elif 75.00 < valor_tempo <= 100:
    print('Intervalo (75,100]')

else:
    print('Fora de intervalo')
