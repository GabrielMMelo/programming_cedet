class Carro():
    def __init__(self, cor, ano, numero_portas):
       self.cor = cor
       self.ano = ano
       self.numero_portas = numero_portas

    def exibir_caracteristicas(self):
        print ("Cor: " + self.cor + " Ano: " + str(self.ano) + " Número de portas: " + str(self.numero_portas))

fusca = Carro("azul", 1942, 2)
fusca.exibir_caracteristicas()
