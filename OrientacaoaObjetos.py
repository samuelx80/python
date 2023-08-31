
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        print("Olá. meu nome é", self.nome,"e eu tenho", self.idade, "anos.")
    
    def aniversario (self):
        self.idade += 1

pessoa = Pessoa ("Maria", 30)
pessoa.apresentar()

nova_pessoa = Pessoa ("João", 40)
nova_pessoa.aniversario()
nova_pessoa.apresentar()

filha_de_maria_e_jose = Pessoa ("Josefina", 12)
filha_de_maria_e_jose.apresentar()


tia = Pessoa ("Margarida", 43)
tia.aniversario()
tia.apresentar()

print ("="*79)

# EXEMPLO DE CLASSE EM PYTHON:
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 

    def acelerar (self):
        print("O carro está acelerando.")
    
    def frear (self):
        print("O carro está freando.")
    
# EXEMPLO DE CRIAÇÃO DE OBJETOS A PARTIR DE UMA CLASSE:
carro1 = Carro("Ford","mustang")
carro2 = Carro("Chevrolet", "Camaro")

# EXEMPLO DE ACESSO A ATRIBUTOS E CHAMADA DE MÉTODOS:
print(carro1.marca)
print(carro2.modelo)

carro1.acelerar()
carro2.frear()

# EXEMPLO DE HERANÇA:
class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, potencia ):
        super().__init__(marca,modelo)
        self.potencia = potencia 

    def turbo (self):
        print("Ativando o turbo!")

    def frase (self):
        print("O carro da marca", self.marca, "de modelo", self.modelo, "tem uma grande potencia de", self.potencia, "cavalos.")

carro_esportivo = CarroEsportivo("Ferrari", "458 Italia", 570)
carro_esportivo.turbo()
carro_esportivo.frase()

print("="*79)

