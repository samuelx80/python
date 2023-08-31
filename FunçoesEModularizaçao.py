
# Primeiro Exemplo (Utilizando o return)
print("=" * 79)
def soma(a,b) :
    return a + b


resultado = soma(10,5)
print (resultado)
print("=" * 79)

# Segundo Exemplo (Utilizando o print no lugar do Return)

def soma2(c,d) :
    print(c,d)

resultado2 = soma("William ","Felipe")
print(resultado2)
print("=" * 79)

# Voltando ao valor do resultado do primeiro exemplo
resultado = soma(33,6)
print(resultado)
print("=" * 79)

# Testando... (Subtração)
def sub(william, felipe):
    return(william - felipe)

alves = sub(80,50)
print(alves)
print("=" * 79)

# Testando (2) (Multiplicação)
def multiplicaçao(sport,recife):
    return(sport * recife)

resultado_multiplicação = multiplicaçao(5,30)
print(resultado_multiplicação)
print("=" * 79)

# Testando (3) (Divisão)
def divisão(palmeiras, sãopaulo ):
    return (palmeiras / sãopaulo)

resultado_divisão = divisão(100,10)
print(resultado_divisão)
print("=" * 79)

# Testando (4) (Divisão Inteira)






print("=" * 79)

# CRIAÇÃO DE UMA FUNÇÃO PERSONALIZADA
def saudação (nome): # Dei entrada na função
    mensagem = f"Olá, {nome}! Seja bem- vindo!" # Criei uma variável para imprimir uma frase
    return mensagem # Retornei uma mensagem

nome_usuario = str(input("Digite seu nome:")) # Criei uma variável para o usuário informa seu nome
resultado_saudaçao = saudação(nome_usuario) # Criei outra variável para conectar o nome da função a variável nome_usuario
print(resultado_saudaçao) # Exibindo a variável
print("=" * 79)

# TESTANDO UMA FUNÇÃO PERSONALIZADA
def esse_sou_eu (x, y, z):
    mensagem2 = f"Olá, sou o {x} e tenho {y} anos. Eu moro em {z}."
    return mensagem2

nome_da_pessoa = str(input("Digite seu Nome:\n"))
idade_da_pessoa = int(input("Qual a sua idade:\n"))
cidade_da_pessoa = str(input("Onde você mora:\n"))

resposta = esse_sou_eu(nome_da_pessoa,idade_da_pessoa,cidade_da_pessoa)
print(resposta)
print("=" * 79)

def funcao():
    variavel_local = "Isso é uma variável local"
    print(variavel_local)

funcao()

print("="*79)

