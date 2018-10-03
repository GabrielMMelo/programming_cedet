class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calculaArea(self):
        return self.base * self.altura

ret1 = Retangulo(2,3)
print(ret1.calculaArea())
