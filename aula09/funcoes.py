
from pymongo import MongoClient

Salao = MongoClient()

bd = Salao.tb


def cadastrar():
    
    nome = input("Nome do cliente: ")
    servico = input("Serviço: ")
    valor = input("Valor: ")
    formaPagamento = input("Pagamento: ")


    bd.tb.insert_one(
    
           {   
            'nome':nome,
            'serviço':servico,
            'valor': valor,
            'formaPagamento': formaPagamento
           }
    )

def consultar():
    nome = input('Digite o nome consultado: ') 
    
    Salao = MongoClient()

    bd = Salao.tb
    
    for item in bd.tb.find({'nome': nome, 'serviço': servico, 'valor': valor, 'formaPagamento':formaPagamento}):
        #print(item['nome'])
        print(item['servico'])
        print(item['valor'])
        print(item['formaPagamento'])



def alterar():
    nome = input('Digite o nome que deseja mudar')
   
    Salao = MongoClient()

    bd = Salao.tb

    bd.tb.update_one({'nome': nome }, #mudar
                         {'$set':{'nome': nome}})  #

    
def delete():
    nome = input('Digite o nome que deseja deletar')
    Salao = MongoClient()

    bd = Salao.tb

    bd.tb.delete_one({'nome': nome})  #mudar
    
    
