
print("Questão 1)\nFaça um programa que peça ao usuário para digitar um número inteiro\
informe se este número é par ou ímpar. Caso o usuário não digite um número\
inteiro, informe que não é um número inteiro.\n")

num_int = input('Digite um numero inteiro: ')

try:
    num_int = int(num_int)
    if num_int % 2 == 0:
        print(f'O Número {num_int} é PAR!')
    else:
        print(f'O Número {num_int} é ÍMPAR!')
except ValueError:
    print('Você não digitou um número, ou o número não é inteiro.')

print('-' * 100,'\n')

# FIM Q1

print("Questão 2)\nFaça um programa que pergunte a hora ao usuário e, baseando-se no horário \
descrito, exiba a saudação apropriada. Ex.\
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.\n")

horario = input('Que horas são (int)? -> ')

try:
    horario = int(horario)
    if 0 <= horario <= 11:
        print('Bom dia!') 
    elif 12 <= horario <= 17:
        print('Boa tarde!')
    elif 18 <= horario <= 23:
        print('Boa noite!')
    else:
        print('Valor fora do Range!')
except ValueError:
        print(f'Valor digitado a não foi um numero inteiro!!')

print('-' * 100,'\n')

# FIM Q2

print('Questão 3)\nFaça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou \
menos escreva Seu nome é curto; se tiver entre 5 e 6 letras, escreva \
Seu nome é normal; maior que 6 escreva Seu nome é muito grande.\n')

nome = input('Digite seu nome: ')
try:
    if not nome.isalpha():
        raise ValueError('O que você digitou cara? O tu já viu nome com numero?')
    
    size_nome = len(nome)

    if size_nome < 4:
        print('Nome Curto!')
    
    elif 5 <= size_nome <= 6:
        print('Nome Normal!')
    
    else:
        print('Nome Grande!')
except ValueError as e:
    print(e)

print('-' * 100,'\n')

# FIM Q3
