n = int(input())

for test in range(n):
    number = input().split(' ')
    x = int(number[0])
    y = int(number[1])
    
    if x > y:
        x,y = y,x
    
    sum_number = 0
    for values in range(x+1,y):
        if values % 2 != 0 : 
            sum_number += values

    print(sum_number)