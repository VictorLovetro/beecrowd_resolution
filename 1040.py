numbers = input().split(' ')
n1 = float(numbers[0])
n2 = float(numbers[1])
n3 = float(numbers[2])
n4 = float(numbers[3])


total_sum = (n1*2)+(n2*3)+(n3*4)+(n4*1)
average = total_sum / 10

if average >= 7:
    print(f'Media: {average:.1f}\nAluno aprovado.')

elif average < 5:
    print(f'Media: {average:.1f}\nAluno reprovado.')

elif 5 <= average <= 6.9:
    exam_grade = float(input())
    new_average = (average + exam_grade) / 2
    print(f'Media: {average:.1f}\nAluno em exame.\nNota do exame: {exam_grade:.1f}')
    if new_average >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {new_average:.1f}')
    
    elif new_average <= 4.9:
        print('Aluno reprovado.')
        print(f'Media final: {new_average:.1f}')
