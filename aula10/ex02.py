#apis

import requests 
import time


cep = input('Digite o CEP: ')
time.sleep
#https://viacep.com.br/ws/06223040/json/

destino = 'https://viacep.com.br/ws/'+ cep + '/json'


resposta = request.get(destino)

if resposta.status_code == 200:
    json = resposta.json()
    
    print('CEP: ', json['cep'])
    print('Logradouro: ', json['Logradouro'])
    print('Bairro: ', json['bairro'])
    print('UF: ', json['uf'])
    print(': ', json[''])

    
    
    
