while True:

    first_note = float(input())
    second_note = float(input())
        
    average = (first_note + second_note) / 2 
    if first_note < 0 or second_note <0 :
        if 0 < average < 10:
            print(f'media = {average:.2f}')
    else:
        print('nota invalida')
        
    continuing = int(input("novo calculo (1-sim 2-nao)"))
    if continuing == 1:
        continue
    else:
        break

    
    
 
