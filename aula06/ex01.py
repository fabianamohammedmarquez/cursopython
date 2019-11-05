#herança. Os atributos da classe dos pais vai para a filha

class Pai():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nacionalidade = 'brasileira'
        
    def falar_portugues(self):
        print('olá, como vai vc?')


class Mae():
    def __init__(self):
        self.nome = ''
        self.idade = 0
        
    def falar_frances(self):
        print('Bonjour')


class Filha(Pai, Mae):
    def __init__(self):
        Pai.__init__(self)
        self.profissao = ''
        
    def falar_portugues(self):
        print('Bonjour, como vai vc?')
        
