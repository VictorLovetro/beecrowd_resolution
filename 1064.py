laps = 6
positive_values = 0
average_values = 0

while laps > 0:
    numbers = float(input())
    laps -= 1
    if numbers > 0:
        positive_values += 1
        average_values += numbers
        if laps == 0:
            final_average = average_values / positive_values

print(f'{positive_values} valores positivos')
print(f'{final_average:.1f}')