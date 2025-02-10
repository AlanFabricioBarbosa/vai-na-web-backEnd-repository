# Esse é um desafio em Python. O desafio é composto por missões. 

#Missão 01:

grade = float(input('Digite a nota do aluno para saber se ele foi aprovado, a aprovação é com 5 ou mais: '))

if grade >= 5:
    print(f'Aluno aprovado com nota: {grade}')
else:
    print(f'Aluno reprovado com nota: {grade}')

#Missão 02:

age = int(input('Para votar, você precisa inserir sua idade, 16 anos ou mais: '))

if age >= 16:
    print(f'Sua idade é {age}. Você pode votar!')
else:
    print(f'Sua idade é {age}. Ainda não pode votar!')

# Missão 03:

def check_studant_grade(grade):
    match grade:
        case g if 90 <= g <= 100:
            print(f'Parabéns, você tirou A com {grade}')
        case g if 80 <= g <= 89:
            print(f'Muito bem, você tirou B com {grade}')
        case g if 70 <= g <= 79:
            print(f'Muito bem, você tirou c com {grade}')
        case g if 60 <= g <= 69:
            print(f'Muito bem, você tirou D com {grade}')
        case g if g < 60:
            print(f'Estude um pouco mais, você tirou F com {grade}')
        case _:
            print('Nota inválida.')

check_studant_grade(float(input('Digite a nota do Aluno de 0 a 100: ')))

#Missão 04: 

first_num = float(input('Digite o primeiro número para ser somado: '))
second_num = float(input('Digite o segundo número para ser somado: '))

sum = first_num + second_num

print(sum)

# Missão 05: 

password = input('Qual a sua senha?')

if password == 'python123':
    print('Acesso permitido!')
else:
    print('Acesso negado!')

# Missão 06: 

num = 0

while num < 10:
    print(num)
    num += 1

#Missão 07: 

list = [8, 3, 10, 1, 5]

print(sorted(list))

#Missão 08:

studants = [

    {'name': 'Alan'},
    {'name': 'Ana'},
    {'name': 'Bruno'},
    {'name': 'Carla'},
    {'name': 'Daniel'},
    {'name': 'Eduardo'},

]

ordered_students = sorted(studants, key=lambda studants: studants['name'])

print("Os alunos são:")

for student in ordered_students:
    print(student['name'])

# Missão 09: 

def double(num):
    return f'O dobro de {num} é {num * 2}'

print(double(int(input('Escolha um número para calcurar o valor de dobro: '))))

# Missão 10: 

def count_letters(name):
    return f'O nome {name} tem {len(name)} letras'

print(count_letters(input('Digite um nome para contar quantas letras ele tem: ')))

