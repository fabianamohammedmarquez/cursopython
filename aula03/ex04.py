
def soma(num1, num2):
    resultado = num1 + num2
    return resultado
    
def sub(num1, num2):
    resultado = num1 - num2
    return resultado

def multi(num1, num2):
    resultado = num1 * num2
    return resultado
    
def div(num1, num2):
    resultado = num1 / num2
    return resultado
        
def main ():
    dic = {'1':soma, '2':sub, '3':multi,'4':div}
    
    n1 = int(input('N1: '))
    n2 = int(input('N2: '))
    opcao = input('o que deseja realizar: 1- soma\n 2- sub\n 3- multiplicaçao\n 4- divisao \n')
    
    print(dic[opcao](n1,n2))
    
if __name__ == "__main__"
    main()
    
    
