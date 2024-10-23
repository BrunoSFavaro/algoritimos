import pandas as pd

cidades = [
    "São Paulo (SP)",
    "Rio de Janeiro (RJ)",
    "Brasília (DF)",
    "Fortaleza (CE)",
    "Salvador (BA)",
    "Belo Horizonte (MG)",
    "Manaus (AM)",
    "Curitiba (PR)",
]

populacoes = [
    12,
    6.5,
    3,
    2.4,
    2.4,
    2.3,
    2,
    1.7
]

cidades_serie = pd.Series(cidades)
# print(cidades_serie)

populacoes_serie = pd.Series(populacoes)
# print(populacoes_serie)


populacoes_serie.max()

# DataFrames
cidades_populosas = pd.DataFrame({'cidade' : cidades_serie, 'populacao em milhoes' :populacoes_serie})
print(cidades_populosas)



area_urbana = [
    '914',
    '640',
    '590',
    '253',
    '196',
    '274',
    '277',
    '336'
]

