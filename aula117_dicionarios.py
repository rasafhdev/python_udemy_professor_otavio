# Dicionário é uma coleção de dados, que é tratada através de chave e valor.

# Forma 1 de criar um dicionário.
dicionario = {}
"Uma variavel recebe um par de chaves para criar um dicionário vazio!"

dicionario = {'Nome': 'Rodrigo'}
"Uma variavel recebe um par chave e valor de strings"

dicionario = {
    'Nome': 'Rodrigo',
    'Sobrenome': 'Asafh',
    'Data nascimento': 1996,
},
"Um dicionário com strings e um numero inteiro"



# Segunda forma:
dicionario_2 = dict()
"Usando a classe dict"

dicionario_2 = dict(nome='Rodrigo')
"No caso do uso na classe é necessário usar argumentos nomeados"

dicionario_2 = dict(
    nome = 'Rodrigo',
    sobrenome = 'Asafh',
    data_nascimento = 1996
)
# Neste caso mesmo que usemos o sinal de =,
# o dicionário vai colocar :.


print(dicionario)
print(dicionario_2)