
import pandas as pd

url = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"

tables = pd.read_html(url)

tabela = tables[1]

tabela.to_excel("Tabela_da_serie_A.xlsx", index=False)

print('Tabela salva com sucesso!')