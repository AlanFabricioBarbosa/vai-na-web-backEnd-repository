#tipos de dados

Variavel = "String" #String
Variavel = 38 #Int
Variavel = 1.3 #Float
Variavel = True #Boolean

# Comparadores

"""
    =
    ==
    !=
    >
    <
    >=
    <=

"""

#Operadores logicos

"""
    and
    or
    not

"""
#Exemplo com or
"""
cadastro = input("Digite seu numero: ")
cadastro = float(cadastro)

if cadastro == 123 or cadastro == 456:
    print('você foi premiado!')
else:
    print('Você não foi premiado')

"""

#exemplo com and

"""

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

if nome == 'Alan' and sobrenome == 'Fabrício':
    print('Nome confirmado')
else:
    print('Nome e Sobrenome errados')

"""
#exemplo com not

"""

pais_de_acesso = 'Sol'

if not pais_de_acesso == 'Sol':
    print('Está claro')
else:
    print('Está escuro')

"""

#Listas

dia = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

#tuplas

frutas = ("Banana", "Uva", "Laranja")

#Dicionarios

alunos = {
    'nome': 'Alan',
    'idade': 20, 
}

#Loops

#for
"""
for i in 'Noite':
    print(i)
"""

#while
"""
num = 1

while num < 10:
    print(num)
    num += 1
"""