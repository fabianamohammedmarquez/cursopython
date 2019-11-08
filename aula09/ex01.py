#mongo db

from pymongo import MongoClient

client = MongoClient()

bd = client.pessoa

#INSERT 

bd.pessoa.insert_many(
    [
       
       {   
        'nome':'Bill Gates',
        'nacionalidade':'Estadunidense',
        'idade': 65
       },
      
       {   
        'nome':'Steve Jobs',
        'nacionalidade':'Estadunidense',
        'idade': 62
       },
      
       {   
        'nome':'Wozniack',
        'nacionalidade':'Estadunidense',
        'idade': 72
       },

    ]
)

