nome_do_dicionario = {
    "chave":"valor"
}

# print(nome_do_dicionario)
# print(type(nome_do_dicionario))

#------------------------

comida = {
    "prato_01" : "salada",
    "prato_02" : "Lasanha",
}

# print(comida)

#----------------------

cadastro = {
    "nome" : "Alan",
    "altura" : "1.85",
    "idade" : "26",
}

cadastro["cidade"] = "Maceió" #Add uma nova chave e valor
cadastro["idade"] = "55" #Add um novo valor

del cadastro["altura"] #deletando uma chave

cadastro.clear() #limpando o dicionario

# print(cadastro)

#--------------------------------

livros = {
    "nome" : "A arte da guerra",
    "autor" : "Sun Tzu",
}

ultimo_item = livros.popitem()

livros.update({"ano" : "500Ac", "editora" : "Japaneses"})

# print(livros)

#-----------------------------

def frase():
    print("Olá Mundo!")

# frase()

#------------------------

def verifica_numero(numero):
    if numero % 2 == 0:
        return f'O numero {numero} é par'
    else:
        return f'O numero {numero} é impar'

resultado = verifica_numero(9)

print(resultado)