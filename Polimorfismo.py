
# Poliformismo por sobrescrita
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

variavel = [Cachorro(), Gato()]

for animal in variavel:
    animal.fazer_som()

print("="*79)

# Poliformismo por Interface

class Forma:
    def area(self):
        pass

class Quadrado (Forma):
    def __init__(self, base, h):
        self.base = base
        self.h = h
    
    def area(self):
        return f"A área do quadrado é: {self.base * self.h}"
    
class Retangulo (Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return f"A área do retangulo é: {self.largura * self.altura}"
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return f"O raio do círculo é: {3.14 * self.raio ** 2}"

class Trapezio(Forma):
    def __init__(self, base_maior, base_menor, altura_do_trapezio):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura_do_trapezio = altura_do_trapezio

    def area(self):
        return f"O valor da área é: {self.base_maior + self.base_menor * self.altura_do_trapezio / 2 }"

formas = [Retangulo (10, 3), Circulo (3), Quadrado (4, 5), Trapezio (43, 30, 4) ]

for forma in formas:
    print(forma.area())