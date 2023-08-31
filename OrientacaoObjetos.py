
# ATIVIDADE
'''
Crie uma classe que tem dois atributos de sua escolha.
Crie dois métodos de sua escolha.
Crie duas classes filhas, que herdam características da classe mãe.
Modifique os métodos de acordo com a necessidade de cada uma.
Imprima os resultados.
'''
class time:
    def __init__ (self, serieA, time):
        self.serieA = serieA
        self.time = time
    
    def frase (self):
        print("O líder da", self.serieA, "é o", self.time)
    

time_serie_A = time ("Serie A", "Botafogo")
time_serie_A.frase()



