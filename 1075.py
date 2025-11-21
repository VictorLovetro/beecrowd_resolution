value = int(input())

for values in range(1,10001):
    if values % value == 2:
        print(values)