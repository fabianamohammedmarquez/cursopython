
#criar uma classe
class Conta_bancaria():
    
    ##criar o construtor 
    def __init__(self, ag=0, cc=0, tit='', saldo=0):   #parametros
        self.__agencia = ag          #__ privad (encapsular)
        self.__conta = cc
        self.__titular = tit      #metodo
        self.__saldo= saldo 

    def saque(self, valor):
        if self.__saldo < valor:
            return'Saldo insuficiente'
        else:
            self.__saldo -= valor
            return self.__saldo
   
    def deposito(self, valor):
        self.__saldo += valor
        print('Deposito realizado!')
        
    def verSaldo(self):
        return self.__saldo
        
    def efetivaTransferencia(self, valor):
        self.__saldo += valor
        
    def transferencia(self, valor, conta):
        if valor > self.__saldo:
            return 'Saldo insuficiente'
        else:
            self.__saldo -= valor
            conta.efetivaTransferencia(valor)

# instancia novo objeto do tipo conta
conta = Conta_bancaria(1123,8897,"Fabi",6000)
conta2 = Conta_bancaria(1111,2222,"Felipe",8000)

#realizar depsito e saque
print(conta.deposito(500))

print(conta.saque(100))
 
#print(conta.saldo)

print(conta.verSaldo())
conta.transferencia(100,conta2)
print(conta2.verSaldo())

