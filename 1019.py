valor_inteiro = int(input())

horas = valor_inteiro // 3600
resto = valor_inteiro % 3600
minutos = resto // 60
segundos = resto % 60

print('{}:{}:{}'.format(horas,minutos,segundos))