
from carro import *
import unittest

class testeCarro(unittest.TestCase):
    
    def test_construtor(self):
        #
        c1 = carro
        self.assertEqual(0, c1.velocidade)
        self.assertEqual(0, c1.ano)
        self.assertEqual('', c1.cor)
        self.assertEqual('', c1.modelo)
        
        #teste construtos com parametros
        c2 = Carro('fusca', 'vermelho', 0, 1975)
        self.assertEqual(0, c2.velocidade)
        self.assertEqual(1975, c2.ano)
        self.assertEqual('vermelho', c2.cor)
        self.assertEqual('fusca', c1.modelo)
    
    def test_funcAcelerar(self):
        c3 = Carro()
        c3.acelerar()
        self.assertEqual(10, c3.velocidade)
        
    def test_funcFrear(self):
        c4 = Carro()
        c4.acelerar()
        c4.frear()
        self.assertEqual(0, c4.velocidade)
        
   
if __name__== '__main__':
   unittest.main()
