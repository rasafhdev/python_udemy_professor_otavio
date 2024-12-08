# Args empacota o que for enviados pela função
# Sintaxe: *args
# convenção: asteristico args

'''
def soma(*args): # faz o enpacotamento em args
    total = 0 # acumulador
    print(args, type(args))
    for numero in args:
        total += numero
        print(f'+ {numero} = {total}')
'''

# Acima foi utilizado o print para poder exemplicar a ação.
# Mas para casos de função, no qual você precisa do valor,
# que foi utilizado com o for, utilizamos o return.

def soma(*args):
    "Soma valores enpacotados em args"
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1,2,3)
soma_4_5_6 = soma(4,5,6)
outra_soma = soma(1,2,3,4,5,6,7,9,10,100,1000,10000) # quantos valores quiser
tupla = (1,2,3,4,5,6,7,9,10,100,1000,10000)



#help(soma)
print(soma_1_2_3)
print(soma_4_5_6)
print(outra_soma)
print(soma(*tupla)) # desempacotamento func soma builtin do python!

