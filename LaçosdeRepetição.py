
# Gerando uma sequência de 0 a 9
print(list(range(10)))

# Gerando uma sequência de 1 a 10
print(list(range(1, 11)))

# Gerando uma sequência numérica negativa
print(tuple(range(0, 30, 5)))

# Gerando uma sequência numérica negativa
print(list(range(0, 101))) # É usado constantemente, porque a lista pode adicionar outro número mais a frente, diferente das tuplas.

# Exemplo (Teste)
print(str(range(0, 50)))

# Percorrendo lista de números
for elemento in range(len("String")):
    print("Estamos no elemento", elemento)


#ATIVIDADE

lista1 = []
lista2 = []
for produto in range (0, 4):
    p = str(input("Digite o nome do produto:"))
    v = float(input("Digite o valor do produto:"))
    lista1.append(p)
    lista2.append(v)
print(lista1)
print(lista2)
print("O valor da compra foi", sum(lista2))

print("*****")

cupom = input("Digite o cupom:")
if (cupom =="Paratibe"):
    print("Voce ganhou 15% de desconto")
else:
    print("Sem desconto!")

print("*****")

# ATIVIDADE 2

lista_roupas = []
lista_valor = []
for vestimento in range(0, 6):
    item = input("Digite o item desejavel:")
    valor = float(input("Qual o valor do item?"))
    lista_roupas.append(item)
    lista_valor.append(valor)
print(lista_roupas)
print(lista_valor)

print("O valor da compra foi:", sum(lista_valor))

lista_geral = []
lista_par = []
lista_impar = []

for o in range(0,21):
    lista_geral.append(o)
    
a = (list(range(0,21)))
print(a)
listpar = (a[0,21,2])
print(listpar)
listimpar = (a[0,21,3])
print(listimpar)






