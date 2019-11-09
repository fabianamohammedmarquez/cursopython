
from funcoes import *

def main():
    while True:
        opcao = input('O que deseja fazer:\n 1-Cadastrar dado\n 2-Consulta dado\n 3-Alterar dado\n 4-Deletar dado\n 5-Sair\n  ')
        
        if opcao == '1':
            cadastrar()
            
        elif opcao == '2':
            consultar()
        
        elif opcao == '3':
            alterar()
            
        elif opcao == '4':
            deletar()
            
        elif opcao == '5':
            break
        else:
            print('opcao invalida')



if __name__ == "__main__":
    main()
