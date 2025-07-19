values_read = int(input())
laps = values_read
in_number = 0
out_number = 0

while laps > 0 :
    int_value = int(input()) 
    laps -=1

    if int_value >= 10 and int_value <= 20:
        if int_value > 0:
                in_number += 1
    else:
        if int_value > 0:
            out_number += 1
print(f'{in_number} in')
print(f'{out_number} out')




