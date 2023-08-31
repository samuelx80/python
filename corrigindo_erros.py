try:
    x=float(input("Escolha um número:"))
    y=float(input("Escolha outro número:"))

    divisao = x/y
    print(divisao)

except ZeroDivisionError as error:
    print("não é possível acessar")