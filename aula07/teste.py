import unittest
from funcoes import*

class testeFuncoes(unittest.TestCase):
    
    def test_funcSoma(self):
        self.assertEqual(4,soma(2,2))
        
    def test_funcSub(self):
        self.assertEqual(2,sub(4,2))

if __name__=='__main__':
    unittest.main()
