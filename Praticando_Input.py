
#Cenário 1
cupom = (input("Digite o cupom:"))

if (cupom=="FUCTURA1" or cupom=="FUCTURA2"):
    print("Você ganhou 15% de desconto")


#Cenário 2
cupom2 = (input("Digite o cupom:"))

if (cupom2=="FUCTURA1" or cupom2=="FUCTURA2"):
    print("Você ganhou 15% de desconto")
else:
    print("Você ganhou 10% de desconto")


#Cenário 3
cupom3 = (input("Digite o cupom:"))

if (cupom3=="FUCTURA1"):
    print("Você ganhou 15% de desconto") 
elif (cupom3=="FUCTURA2"):
    print("Você ganhou 10% de desconto")
else:
    print("Você ganhou 5% de desconto")


#Cenário 4
cupom4 = (input("Digite o cupom:"))

if (cupom4=="FUCTURA"):
    print("Você ganhou 15% de desconto")
elif (cupom4=="FUCTURA1"):
    print("Você ganhou 10% de desconto")
elif (cupom4=="FUCTURA2"):
    print("Você ganhou 5% de desconto")
else:
    print("Cupom Inválido")