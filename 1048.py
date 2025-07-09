salario_funcionario = float(input())
def salario(salario,percentual):
    reajuste = salario*(percentual/100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {percentual} %')

if salario_funcionario <= 400:
    salario(salario_funcionario, 15)
elif salario_funcionario <= 800:
    salario(salario_funcionario, 12)
elif salario_funcionario <= 1200:
    salario(salario_funcionario, 10)
elif salario_funcionario <= 2000:
    salario(salario_funcionario, 7)
else:
    salario(salario_funcionario, 4)
    