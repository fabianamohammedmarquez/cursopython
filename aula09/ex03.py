#update

from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

bd.pessoa.update_one({'nome': 'Wozniack'}, 
                     {'$set':{'nome': 'John', 'idade': 22}})
