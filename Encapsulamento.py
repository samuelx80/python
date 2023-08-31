
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome} e eu tenho {self.idade} anos. ")
p = Pessoa ("Alice", 25)
p.apresentar()
print(p.__nome)

print("="*79)

class Inss:
    def __init__(self, nome, idade, potencia):
        self.__nome = nome
        self.__idade = idade
        self.__potencia = potencia

    def get_nome (self):
        return self.__nome
    
    def set_nome (self, novo_nome):
        self.__nome = novo_nome

    def get_idade (self):
        return self.__idade
    
    def set_idade (self, nova_idade):
        self.__idade = nova_idade

    def get_potencia (self,):
        return self.__potencia
    
    def set_potencia (self, nova_potencia):
        self.__potencia = nova_potencia

p = Inss ("Alice",25, 456)
print(p.get_nome())
print(p.get_idade())
print(p.get_potencia())
frase = F"{p.get_nome()} tem {p.get_idade()}, possui um carro muito bonito e com uma potencia de {p.get_potencia()} cavalos"
print(frase)

p.set_nome("Bob")
print(p.get_nome())

p.set_idade("43")
print(p.get_idade())




