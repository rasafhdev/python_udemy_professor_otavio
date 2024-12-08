"""
Exercício
Usuário deveria inserir: Nome e Idade
Se o nome e a idade forem forem digitadas:
Exbiba:
    Seu nome é: ...
    Seu nome invertido é: ...
    Seu nome contem (ou não), x espaços
    SEu nome tem x letras
    A primeira letra do seu nome é:
    A ulitma letra do seu nome é:
"""

#nome = input('Digite seu nome: ')
#idade = input('Digite sua idade: ')

nome = 'Rodrigo'
idade = 28

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaço!')
    else:
        print('Seu nome não contém espaço!')

    print(f'Quantidade de letras do seu nome: {7}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Algum valor não foi digitado')
