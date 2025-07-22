values = input().split(' ')

a = int(values[0])
b = int(values[1])
value_a = max(a,b)
value_b = min(a,b)
if value_a %value_b  == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')