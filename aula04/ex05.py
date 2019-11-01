

cpf = input('Digite o cpf: ')
with open ('dados.txt') as f:
    conteudo = f.readlines()
    
    
for registro in conteudo:
    if cpf in registro:
        saida = registro.split(';')
        print('cpf: ', saida[0])
        print('nome: ', saida[1])
        print('idade: ', saida[2])



exit()
nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
cpf = input('Digite o cpf: ')

registro = nome+';'+idade+';'+cpf

with open('dados.txt', 'w') as f:
    f.write(registro)
