laps_count = 0
count_of_pair = 0

while laps_count < 5:
    laps_count += 1
    values = int(input())
    if values % 2 == 0 :
        count_of_pair += 1
print(f'{count_of_pair} valores pares')