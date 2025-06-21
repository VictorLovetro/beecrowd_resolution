salary = float(input())

total_tax = 0

def calculate_tax(start, end, value, tax):

    #exemplo de entrada:
    #start = 2000
    #end = 3000
    #valor = 2500
    #tax = 10

    min_value = min(value, end) # neste caso pegar o menor valor, por exemplo entre os valores 2500(parametro `value`) e 3000 (parametro `end`), ele vai pegar o 2500(parametro `value`).
    max_value = max(start, min_value) # neste caso pegar o maior valor, por exemplo entre os valores 2000(parametro `value`) e 3000 (parametro `end`), ele vai pegar o 3000(parametro `end`)

    print("range_value:", max_value) # aqui vai ter o valor 3000(parametro `end`)

    pre_value = max_value if end > 0 else value # aqui acontece a tomada de decicao para escolhe se vai usar o max_value,

    print("pre_value:", pre_value) # aqui vai ter o valor 3000(parametro `end`)

    final_value = pre_value - start # aqui pegar o valor a ser calculado a tax, neste exemplo 3000(variavel pre_value) subtrair 2000(parametro `start`)

    print("final_value:", final_value) # aqui o resultado de 3000 - 2000 = 1000

    tax_value = final_value * (tax / 100) # aqui convertamos o valor do parametro `tax` para porcentagem e usamos para calcular a taxa encima do valor da variavel `final_value`

    print("tax_value:", tax_value) # aqui o resultado de 1000 * (8 / 100) = 40.0

    print()

    return tax_value # aqui retorna a taxa calculada

if salary >= 2000.01:
    total_tax += calculate_tax(end=3000, start=2000, value=salary, tax=8)

if salary >= 3000.01:
    total_tax += calculate_tax(3000, 4500, salary, 18)

if salary >= 4500.0:
    total_tax += calculate_tax(4500, 0, salary, 28)

print("total_tax:", total_tax)