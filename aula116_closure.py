'''
Closure e funções que retornam outras funções.
'''

def cirar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar # estamos adiando a função cirar_saudacao

falar_bom_dia = cirar_saudacao('\nBom dia')
falar_boa_tarde = cirar_saudacao('Boa tarde')
falar_boa_noite = cirar_saudacao('Boa noite')

for nome in ['Rodrigo', 'Patricia', 'Helena']:
    print(falar_bom_dia(nome)) #closure
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))