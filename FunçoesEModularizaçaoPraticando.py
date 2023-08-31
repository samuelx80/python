
# EXERCICIO (1)


def soma(j, k):
    return j + k

mensagem_exercicio1 = soma(40,10)
print(mensagem_exercicio1)


print("="*79)

# O professor sugere que os códigos estejam dentro da função como este exemplo:

def soma():
    l=int(input("Digite um número:"))
    m=int(input("Digite outro número:"))
    return (f'O resultado de é:{l + m}') 

resultado1 = soma()
print(resultado1)

print("=" * 79)

# EXERCICIO (2)

def temperatura ():
    c = float(input("Qual a temperatura em Celsius nesse momento? \n"))
    return (1.8 * c + 32)


calculo = temperatura ()
print("Então, o valor para Fahrenheit é:",calculo)

print("=" * 79)

# EXERCICIO (3)

def is_par():
    valor = int(input("Digite um valor:"))
    if valor % 2 ==0:
        return f"O valor é par!"
    else:
        return f"O valor é impar!"

resultado_par = is_par()
print(resultado_par)

print("="*79)

# EXERCICIO (4)

def lista():
    valor1 = input("Digite uma lista de números:") # Criei uma variável para o usuario digitar uma lista de números
    outra_variavel = valor1.split(",") # Criei outra variavel
    lista_Vazia = []
    for i in outra_variavel:
        lista_Vazia.append(int(i))
    variavel_max = max(lista_Vazia)
    return f"O valor máximo é: {variavel_max}"

variavel_max = lista()
print(variavel_max)

print("="*79)

# EXERCICIO (5)
def fatorial ():
    x = int(input("Digite um valor: "))
    y = 1
    for i in range(1, x+1):
        y=y*i
    return f"O resultado da fatorial é: {y}"

resultado_fatorial = fatorial()
print(resultado_fatorial)

print("="*79)

# EXERCICIO (6)
def invertida():
    nome = input("Digite um nome:")
    return f" O resultado é:{nome [::-1]}"

a = invertida()
print(a)

print("="*79)

# EXERCICIO (7)
def lista_numeros():
    lista = []
    numeros = input("Digite os números:")
    variavel = numeros.split(",")
    for elemento in variavel:
        lista.append (int(elemento))
    media = sum(lista) / len(lista)

    return f"A média da lista é: {media}" 

resultado_media = lista_numeros
print(resultado_media)

print("="*79)

# EXERCICIO (8)
def lsdf_s():
    texto = input ("Digite uma frase:")
    lista = []
    variavel_x = texto.split(" ")
    for i in variavel_x:
        if len(i) > 5:
            lista.append(i)
    return f"A quantidade de strigs com mais de 5 caracteres é: {len(lista)}"

resultado_x = lsdf_s
print(resultado_x)
print("="*79)


# Atividade
'''
Passando o projeto do banco para funções!
'''
listaNome = []
listaValor = [50]

def conta ():
    nome = str(input('qual é o seu nome: '))
    cpf = str(input('digite o seu cpf: '))
    listaNome.append(nome)

def saldo ():
    saldo = float(input('digite um valor: '))
    listaValor.append(saldo)
    print('seu nome é:', listaNome[0])
    print('seu saldo é:', listaValor[0])

def depósito():
    valor = float(input('digite um valor: '))
    soma = listaValor[0] + valor
    listaValor[0] = soma
    print('seu novo saldo é:',soma)

def encerramento ():
    print('volte sempre!')

def saque ():
    valor = float(input('infome o seu valor de saque: '))
    if valor <= listaValor [0]:
        menos = listaValor[0] - valor
        print('seu novo saldo é:',menos)
    else:
        listaValor [100] <= valor
        print('seu novo saldo é:',valor)
    
while True:
    print('............')
    print('selecione uma opcao')
    print('1 para  criar conta')
    print('2 verificar saldo')
    print('3 depositar dinheiro')
    print('4 sacar dinheiro')
    print('5 encerrar')
    opcoes = str(input('opcao: '))
    if opcoes == '1':
         conta ()
    elif opcoes == '2':
        saldo ()
    elif opcoes == '3':
        depósito ()
    elif opcoes == '4':
        saque ()
    elif opcoes == '5':
        encerramento ()
        break
    else:
        print("Selecione uma opção valida")