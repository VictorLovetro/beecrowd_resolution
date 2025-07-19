true_notice = 0
average_notice = 0
while True:
    notice = float(input())
    if notice > 0 and notice <= 10:
        true_notice += 1
        average_notice += notice
        if true_notice == 2:
            final_average = average_notice / 2
            print(f'media = {final_average:.2f}')
            break
    else:
        if notice < 0 or notice > 10:
            print('nota invalida')


        
