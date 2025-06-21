def table(amount,price):
    total = amount * price
    print(f'Total: R$ {total:.2f}')
    return total

quest =input().split(' ')
code = int(quest[0])
amount = int(quest[1])


if code == 1:
    table(amount, 4)

elif code == 2:
    table(amount,4.50)

elif code == 3:
    table(amount, 5)

elif code == 4:
    table(amount,2)

elif code == 5:
    table(amount,1.50)

