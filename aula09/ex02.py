
from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

#busca geral
for registro in bd.pessoa.find():
    print(registro)

for item in bd.pessoa.find({'nome': 'Bill Gates'}):
    print(item['nome'])
