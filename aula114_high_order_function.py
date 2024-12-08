# High Order Fuctions - Funções de primeira classe.


def saudacao(msg):
    """
    Define uma função de saudação,
    que recebe um parametro como mensagem.
    """
    return(msg)

def executa(funcao, texto):
    """
    Uma funçãoq ue vai retornar a
    funcao saudacao para ser executada
    """
    return funcao(texto)

v = executa(saudacao, 'Bom dia')
print(v)


# Primeiro definimos a funcao executa, que retorna uma mensagem.
# A mensagem checa através da função executa, que é reponsavel
# executar a função saudacao.