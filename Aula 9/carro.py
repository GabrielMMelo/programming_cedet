class Carro():
    def __init__(self, rodas, janela, porta_mala, tipo_combustivel, cor, ano, numero_portas):
       self.cor = cor
       self.ano = ano
       self.numero_portas = numero_portas
       self.rodas = rodas
       self.janela = janela
       self.porta_mala = porta_mala
       self.tipo_combustivel = tipo_combustivel

    def exibir_caracteristicas(self):
        print ("Cor: " + self.cor + " Ano: " + str(self.ano) + " Número de portas: " + str(self.numero_portas))

fusca = Carro("azul", 2)
fusca.exibir_caracteristicas()
