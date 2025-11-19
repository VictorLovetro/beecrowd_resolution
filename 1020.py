idade_dia = int(input())

ano = idade_dia // 365
resto = idade_dia % 365
mes = resto // 30
dia= resto % 30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano,mes,dia))
 