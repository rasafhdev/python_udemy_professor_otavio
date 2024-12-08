# Execícios com funções
'''
Questão1) Crie um função que multiplica todos os argumentos não nomeados.
    - Retorne o total para uma variavel mostra o valor da variavel.

Questão 2) Crie uma função que fala se um número é par ou impar.
    - Retorne se o numero é par o impar.
'''

def multiplicador(*args): # Questão 1)
    "Resultado da primeira questão: Multiplicador"
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(numero): # Questão 2
    "Resultado da segunda questão: Par ou Impar"
    if numero % 2 == 0:
        return f'{numero}: É par!'
    return f'{numero}: É impar!'


# chamada das funções
resultado_multiplicador = multiplicador(1, 2, 3, 4, 5, 6, 8, 9, 10)
resultado_par_impar = par_impar(123)


print(f'O Resultado multiplicação: {resultado_multiplicador}')
print(resultado_par_impar)