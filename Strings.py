# Atenção : Use o print pra retornar o valor das variáveis!
# Declarando uma string

mensagem = "Hello, world!"

# Concatenando strings:
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + "" + sobrenome
nome_completo2 = primeiro_nome + sobrenome


# Acessamento caracteres individuais em uma string:
mensagem = "Hello, world!"
primeiro_caractere = mensagem[0]
ultimo_caractere = mensagem [-1]

# Encontrando o comprimento de uma string


# Convertendo uma string para letras maiúsculas ou minúsculas
mensagem = "Hello, World!"
maiuscula = mensagem.upper()
minuscula = mensagem.lower()
#Dividindo uma string em substrings com base em um delimitador
mensagem = "Hello, World!"
palavras = mensagem.split(",")

""" Atividade, O usuario vai informar seu nome. Não importa a forma que ele vai fazer isso (aSsIm, Desse jeito, OU ESSE ... TANTO faz.)
Preciso inserir esse nome em uma lista.
"""
lista = []
nome = (input("Qual o seu nome?"))
#maiuscula = nome[0].lower()
nome= nome.capitalize()
print(nome)

#Ou

lista = []
nome = input('Qual o seu nome?')
nome_lista = nome[0].upper() + nome[-1:].lower()

lista.append(nome_lista)
print(lista)

# Dividindo uma string em substrings com base em um delimitador:
mensagem = "Hello, world!"
palavras = mensagem.split(",")
print(palavras)

print("*****")
# Verificandp se uma substring está presente em uma string
mensagem = "Hello, world!"
if "world" in mensagem:
    print("A substring 'world'está presente na mensagem." )
print("*****")
# Substituindo caracteres em uma string
mensagem = "Hello, world!"
nova_mensagem = mensagem.replace("world", "Python")
print(nova_mensagem)
print("*****")

# Formatando uma string
nome = "João"
idade = 30
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
mensagem2 = f"Meu nome é {nome} e eu tenho {idade} anos."
print("*****")

# Utilizando caracteres de escape em uma string
mensagem = "Eu gosto de programar em Python! \nEle é uma linguagem muito poderosa."
print(mensagem)
print("*****")

#Covertendo uma string em um número
numero_string = "123"
numero_inteiro = int(numero_string)
numero_float = float(numero_string)
print(numero_string,numero_inteiro,numero_float)
print("*****")

# Acessando substrings de uma string:
mensagem = "Hello, world!"
substring = mensagem[0:4] #Retorna os primeiros cinco caracteres
print(substring)
print("*****")

# Removendo espaços em branco de uma string:

frase = "  Hello, world! "
sem_espacos = frase.strip() 
print(sem_espacos)