salary = float(input())

if 0 <= salary <= 2000:
    print("Isento")

elif 2000.01 <= salary <= 3000:
    tax = (salary - 2000) * 0.08
    print(f'R$ {tax:.2f}')

elif 3000.01 <= salary <= 4500:
    tax = ((salary - 3000) * 0.18) + 80
    print(f'R$ {tax:.2f}')

elif 4500.01 <= salary <= 5500:
    tax = ((salary - 4500) * 0.28) + 350
    print(f'R$ {tax:.2f}')

else:
    tax = ((salary - 5500) *  0.38) + 630
    print(f'R$ {tax:.2f}')


