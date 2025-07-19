fixed_password = '2002'
while True:
    user_input = input()

    if fixed_password != user_input:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        break

