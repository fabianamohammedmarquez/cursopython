
class Onibus (): 
    
    def __init__(self, capacidade = '', origem = '', destino = '', velocidade = ''):
        self.capacidade = capacidade
        self.origem = origem 
        self.destino = destino
        self.velocidade = velocidade 
    
    def embarcar(self):
        if  self.capacidade == 20:
          print('Onibus está cheio')
        else:
            self.capacidade += 1 
    
    def acelerar(self):
        self.velocidade += 20
        
    def frear(self):
        self.velocidade -= 20

Onibus = Onibus(2, 'Vila Mariana', 'Cotia', 30) 

print(Onibus.capacidade)
print(Onibus.origem)
print(Onibus.destino)
print(Onibus.velocidade)


Onibus.acelerar()
Onibus.frear()
print(Onibus.velocidade)
