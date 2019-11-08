
from pymongo import MongoClient

Salao = MongoClient()

bd = Salao.tb


def cadastrar():
    


    nome = input("DIGITE")
    nome = input("DIGITE")
    nome = input("DIGITE")
    nome = input("DIGITE")


    bd.tb.insert_one(
        
           
           {   
            'nome':nome,
            'servico':servico,
            'valor': valor,
            'formaPagamento': pagamento
           }
        
    )

def alterar():
    from pymongo import MongoClient

    client = MongoClient()

    bd = client.pessoa

    bd.pessoa.update_one({'nome': 'Wozniack'}, #mudar
                         {'$set':{'nome': 'John', 'idade': 22}})  #

    
