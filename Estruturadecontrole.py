
produto = 0
while produto != 4:
    p = input("Digite o nome do produto:")
    v = float(input("Digite o valor do produto:"))
    produto = int(input("Digite o valor:"))

# Percorrendo lista de números
elemento = 0
while elemento<=len([1, 2, 3, 4, 5, 6]):
    print("Estamos no elemento", elemento)
    elemento +=1

# Percorrendo uma string
s = 'STRING'
indice = 0
while indice in range(len(s)):
    print("Estamos no elemento", s[indice])
    indice +=1


# Brake
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i = i + 1

#Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)