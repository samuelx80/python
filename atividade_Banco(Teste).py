
# Primeira parte
print("=" * 30)
print("{:^30}".format("Seja bem vindo ao seu banco!"))
print("=" * 30)
# Segunda Parte:
dicionario_nome = {0} 
dicionario_valor = {0}
print("=" * 5)
print("MENU:")
print("=" * 5)
print("1.Criar Conta")
print("2.Verificar Saldo")
print("3.Depositar Dinheiro") 
print("4.Sacar Dinheiro")
print("5.Encerrar o Atendimento")
print("=" * 5)
opcoes = input("Qual opção?\n")
if (opcoes == "1"):
    nome = input("Digite seu nome:")
    saldo = float(input("Digite o seu saldo:"))
    dicionario_nome.append(nome)
    dicionario_valor.append(saldo)

elif opcoes == "2":
    print("Seu saldo é:",dicionario_valor[0])
    print("Seu nome é:",dicionario_nome[0])

elif opcoes =="3":
    deposito = int(input("Qual dinheiro você deseja deposita?\n"))
    dicionario_valor[0] =+ deposito
    print("Seu saldo é:", dicionario_valor[0])

elif opcoes == "4":
    sacar = int(input("Qual o valor você deseja sacar?\n"))
    if (sacar >= dicionario_valor[0]):
        print("Saldo Insuficiente!")
    else:
        dicionario_valor[0] -= sacar
        print("Seu saldo é:", dicionario_valor[0])
else:
    opcoes == "5"
    print("Encerrar o atendimento")




'''
try:
    tipo_conta =  dicionario["tipo_conta"]
    print("O tipo da conta é:",tipo_conta)

except KeyError:
    print("A chave 'tipo_conta' não existe no dicionario. ")


numero_conta = input("Informe o número da conta: ")
if not numero_conta.isdigit():
    print("O número da conta deve ser numérico. Tente novamente.")
    exit()

dicionario = {
    "numero_conta": numero_conta,
    "titular": input("Informe o titular: "),
    "tipo_conta": input("Informe o tipo da conta: ")
}

print("Dados da conta:")
print("Número da conta:", dicionario["numero_conta"])
print("Titular da conta:", dicionario["titular"])
print("Tipo da conta:", dicionario["tipo_conta"])
'''
'''
#Variaveis necessarias
saldo_cliente =  
# Valor sacado
valor_sacado = int(input("Qual o valor que você deseja sacar?"))
saldo_atual = saldo
'''