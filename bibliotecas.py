
import pandas as pd

# URL da página da Wikipedia 
url = "https://pt.wikipedia.org/wiki/lista_de_filmes_de_maior_bilheteria"

# Extrair as tabelas da página
tables = pd.read_html(url)

# Acessar a tabela desejada (no caso, a primeira tabela)
tabela = tables[0]

# Salvar a tabela em um arquivo excel
tabela.to_excel("biblioteca_exemplo1.xlsx", index=False)

print("Tabela salva com sucesso!")