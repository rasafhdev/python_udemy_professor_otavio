# Funções, arugmentos nomeados e não nomeados

def soma(x, y): # x e y são parametros. 
    print(x + y)

soma(1, 2)
# 1 e 2 são os argumentos não nomeados passados para os parâmetros na definição da função.
# Além disso, é necessário tomar cuidado, pois a ordem importa.
# No exemplo acima, nada será afetado porque trata-se de uma simples soma.

soma(y=2, x=1)
# Também é possível realizar a troca da posição, mas é necessário sempre usar o argumento posicional.

soma(x=1, y=2)
# No exemplo acima, estão os arquivo nomeados.
# É sempre necessário tomar cuidado, pois quando são passados argumentos nomeados, o seguinte sempre deverá ser nomeado.
# Portanto:

def soma2(x, y, z):
    print(x + y + z)

soma2(10, y=20, z=30)
# O exemplo acima mostra que ao uusar o argumento nomeado no y, o z também precisar ser nomeado.
# Caso não for passado o SyntaxError será levantado: SyntaxError: positional argument follows keyword argument: soma2(10, y=20, 30)
