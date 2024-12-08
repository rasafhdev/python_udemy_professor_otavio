import pandas as pd

# Tente usar o delimitador ';' e um encoding adequado
df = pd.read_csv('data.csv')

# Lista de nomes a ser procurada
nomes_lista = [
    'NELIE',
    'SERGIO DA SILVA ALVES',
    'ALINE ANANDI',
    'RENATA PEREIRA DE GODOY',
    'Lisia Goulart',
    'Aurea Maria Xavier',
    'ERIKA CESARIO DA SILVA PESSOA ',
    'Renato'
]

# Criar uma expressão regular a partir da lista de nomes
pattern = '|'.join(nomes_lista)

# Filtrar as linhas onde qualquer nome da lista aparece na coluna 'Nome' e selecionar as colunas desejadas
result = df[df['Nome'].str.contains(pattern, case=False, na=False)][['Nome', 'Lotacao', 'LIQUIDO']]

# Exibir o resultado
print(result)


