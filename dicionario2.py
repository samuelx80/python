#Criando um dicionário vazio
dicionario = {}

#Criando um dicionario com alguns pares de chave-valor
dicionario = {"nome":"João", "idade":30, "cidade":"São Paulo"}

#Declarando dicionarios
dic = {}
print(type(dic)) # O type informa o tipo de variavel
dic_pernambuco = {"sport":41,"santa Cruz":29,"nautico":21}
print(dic_pernambuco)

print("*****")

#Adicionando um elemento no dicionario (chave:valor)
# Onde a chave é 'Salgueiro' e o valor é 1
# Note que a chave é passada dentro de colchetes, após o nome do dicionario

dic_pernambuco["salgueiro"] = 1
print(dic_pernambuco)
dic_pernambuco["america"] = 7
print(dic_pernambuco)
dic_pernambuco["sport"] = 43
print(dic_pernambuco)

print("*****")
#Buscando valor com base na chave
quantos_titulos = dic_pernambuco.get("sport") #Forma correta, ajuda a armazenar o valor a uma variavel
print(quantos_titulos)
print(dic_pernambuco["sport"]) # Só faz exibir o valor, não é a maneira correta
print("O Sport tem",quantos_titulos,"titulos")

print("*****")

#Remover um elemento com base na chave
del dic_pernambuco["salgueiro"] #exlui o valor do dicionario e não armazenar o valor em lugar nenhum vai ao espaço
print(dic_pernambuco)

#Remove a chave e retorna seu valor
valor = dic_pernambuco.pop("nautico") #Exclui, mas consegue armazenar o valor em outro lugar(lixeira)
print("O valor retornando da chave é:",valor)
print(dic_pernambuco)

print("*****")
#Verificar se uma chave existe no dicionario
print("santa Cruz" in dic_pernambuco)

print("******")

#Pegar todas as chaves do dicionário
print(dic_pernambuco.keys())

#Pegar todos os valores do dicionário
teste = dic_pernambuco.values()
print(teste)

print("*****")

dic_paulista = {"corinthians":29,"palmeiras":22,"santos":22}

# Removendo e retornando último elemento

print(dic_paulista.popitem())
print(dic_paulista)

print("*****")

#Mesclar dois dicionários
dic_pernambuco.update(dic_paulista)
print(dic_pernambuco)

print("*****")

#Convertendo um dicionário em uma lista
print(list(dic_pernambuco))
print(list(dic_pernambuco.values()))

