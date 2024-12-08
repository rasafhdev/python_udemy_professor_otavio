# Faça um programa para ler um numero, e na sequência dobralho.
# Não se esqueça de fazer o tratamento de erro, com Try - Except


n = input('Digite um numero: ')
n2 = n

try:
    n = float(n)
    print(f'O número digitado foi {n}, seu dobro é: {n * 2}')
except:
    print('Não foi digitado um número!')

# Minha forma

try:
    if n2.isnumeric():
        n2 = float(n2)
        print(f'Minha forma: O dobro de {n2}, é: {n2 * 2}')
except ValueError:
    print('Você não digitou um número')
