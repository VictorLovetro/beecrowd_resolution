value_of_turns = int(input())
lap_counter = value_of_turns

while lap_counter > 0:
    numbers_check = int(input())
    lap_counter -=1
    if numbers_check > 0 :
        if numbers_check % 2 == 0:
            print('EVEN POSITIVE')
    elif numbers_check < 0:
        if numbers_check % 2 == 0:
            print('EVEN NEGATIVE')
    if numbers_check > 0:
        if numbers_check % 2 != 0:
            print('ODD POSITIVE')
    elif numbers_check <0:
        if numbers_check % 2 != 0:
            print('ODD NEGATIVE')
    else:
        print('NULL')