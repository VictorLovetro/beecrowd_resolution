while True:
    while True: 
            primeira_nota =  float(input())
            if 0 < primeira_nota <= 10: 
                break
            else:
                print('nota invalida')

    while True:
        segunda_nota = float(input())
        if 0 < segunda_nota <= 10:
            media = (primeira_nota + segunda_nota) / 2
            print(f'media = {media:.2f}')
            break
        else:
            print('nota invalida')


    while True:
        print("novo calculo (1-sim 2-nao)")
        resposta_usuario = int(input())
        if resposta_usuario == 1:
            break
        if resposta_usuario == 2:
            break
    if resposta_usuario == 2:
        break
    
 
