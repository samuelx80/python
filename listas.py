
#Declarando uma lista vazia em python
lista1 = []

lista1 = [1,"2",3] #CRIANDO UMA LISTA
print(type(lista1),lista1)

#Declaração explícita de lista
lista2 = list((1,"2",3))
print(lista2)

#Declaração implícita                               # [Elementos de outra lista, mas vai ser outra lista. Além disso vai ser o 5 índice da lista 3]        
lista3 = ["c", 4.65, True, "True", "Vamos aprender", ["outra", "lista", "interna"], lista2]
print(lista3)

lista4 = ["primeiro","segundo","terceiro"]
print(lista4)
print(lista3 [2])
print(lista1 [0])
print(lista3 [6])
print(lista3 [4][1])
print(lista3)

print("***********************************************************************")

#**Fatiando Listas**

#Execute cada um por vez
print(lista3)
print(lista3[2:6:2])
print(lista3[:3])
print(lista3[-1:])
print("Imprimindo de dois em dois:", lista3[::2])
print(lista3[::])
print(lista3)
print(len(lista3[5][2]))
print(len(lista2))
print("***********************************************************************")
print(lista1)
lista1.append("Python")
lista1.append("Java")
lista1.append("C#")
lista1.append("Php")

#lista1.append("Python, Java, C#") #Teste. So tem uma linha e corresponde a 1 elemento

print(lista1)

lista1.insert(2,"C++")
print(lista1)


#Remover um elemneto pelo seu valor
lista1.remove("Java")
print(lista1)

#Indexação (Pegar um índice de um elemento pelo valor)
indice = lista1.index("Php")
print(indice)

#Remover um elemento pelo seu indice
del(lista1[indice])
del(lista1[5])
print(lista1)

print("Lista Original:", lista4)

#Invertendo uma lista
lista4.reverse()
print("Lista invertida:", lista4)

#Ordenando uma lista
lista4.sort()
print("Lista Ordenada:", lista4)

#Comprimento de uma lista
print(lista1, len(lista1), "elementos")
print(lista2, len(lista2), "elementos")
print(lista3, len(lista3), "elementos")
print(lista4, len(lista4), "elementos")

#Alterando um valor de uma lista

l = [6,7,5,8,9]
v = l
print(v)
print(l)


#Testando se de fato é uma cópia
v[0]=-100
print(v)
print(l)

#Forma correta de copiar listas
l=[6,7,5,8,9]
v=l[:]
z=list(l)

print(l,v,z)

print("***********************************************************************")


