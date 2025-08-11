individual_age = 0
counter = 0
while True:
    age = float(input())
    if age > 0:
        counter += 1
        individual_age += age
    if age < 0 :
        break
media = individual_age/ counter
print(f'{media:.2f}')

