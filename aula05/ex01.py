
#funcao cadastro
def cadastro():
    cpf = input('Digite o cpf: ')
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    uf = input('Digite o uf: ')
    registro = cpf+';'+nome+';'+email+';'+uf
    
    with open('dados.txt', 'w') as f:
        f.write(registro)


#consulta

def consulta():
    cpf = input('Digite o cpf: ')
    with open ('dados.txt') as f:
        # ['XXX;XXXX;XXX', 'XXXX;XXX' ...]
        conteudo = f.readlines()
    
    for registro in conteudo:
        if cpf in registro:
            saida = registro.split(';') # ['cpf', 'nome', 'email', 'uf]' 
            print('cpf: ', saida[0])    #    0       1      2        3
            print('nome: ', saida[1])
            print('email: ', saida[2])
            print('uf: ', saida[3])
            
def main():
    while True:
        opcao = input('O que deseja fazer?\n 1-Cadastrar\n 2-Consultar\n 3-Sair\n ')
        if opcao == '1':
            cadastro()
        elif opcao == '2': 
            consulta()
        elif opcao =='3':
            break
        else:
            print('Opcao invalida')


if __name__ == "__main__":
    main()
