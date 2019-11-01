#arquivos

with open('arquivo.txt', 'r') as f:
    conteudo = f.read()


print(conteudo)     
#conteudo = conteudo.split(';')
#print(conteudo[0].split(';')) 
#print(type(conteudo))


registro = 'fabi;15;33.222.11-25'

with open ('arquivo2.txt', 'a') as f:
    f.write(registro)
