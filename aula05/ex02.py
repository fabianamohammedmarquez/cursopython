#classes


class Carro():
    
    #construtor
    
    def __init__(self, modelo = '', cor = '', velocidade = '', ano = ''):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade
        self.ano = ano
        
    def acelerar(self):
        self.velocidade += 10
        
    def frear(self):
        if self.velocidade == 0:
            print('o carro esta parado')
        else:
            self.velocidade -= 10
#crie um objeto

fusca = Carro('fusca','vermelho', 0, 1975)
brasilia = Carro('brasilia', 'amarela', 0, 1985)
verona = Carro()

print(fusca.modelo)
print(fusca.cor)
print (fusca.velocidade)

fusca.acelerar()
fusca.acelerar()

print(fusca.velocidade)
