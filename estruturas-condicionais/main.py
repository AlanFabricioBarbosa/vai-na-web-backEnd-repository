saldo = False

if saldo == False:
    print("Saldo negativo")

#--------------------------

idade = 16

if idade >= 18:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")

#--------------------------

salario = True
idadeDoUsuario = 18

if idadeDoUsuario >= 18 and salario == True:
    print("Você tem idade para dirigir e salario")
elif idadeDoUsuario < 18 and salario == False:
    print("Você não tem dinheiro e não tem idade")
else:
    print("Não precisa de carteira no VNW")

#--------------------------

def semana(dia):
    if(dia == 1):
        print("Segunda-feira")
    elif(dia == 2):
        print("Terça-feira")
    elif(dia == 3):
        print("Quarta-feira")
    else:
        print("Error")

semana(1)

#--------------------------

cargo = input("Digite um cargo:  ")

if cargo == "admin" or cargo == "gerente":
    print("Acesso liberado!")
else:
    print("Acesso Negado!")


#--------------------------

for caractere in "Python":
    print(caractere)

#--------------------------

lista_de_sonhos = ["Iate", "Avião", "Ferrari", "Resort"]

for i in lista_de_sonhos:
    print(i)

#--------------------------

contador = 0

while contador < 10:
    print(contador)
    contador += 1

#--------------------------

lanche = "Pizza"

print(lanche[0])
print(lanche.upper())
print(lanche.lower())
