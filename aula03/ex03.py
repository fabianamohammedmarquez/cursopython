
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
        
def main():
    valor1 = float(input("Digite o valor: "))
    valor2 = float(input("Digite um segundo valor: "))
    operacao = input("o que deseja realizar: 1- soma\n 2- sub\n 3- multiplicaçao\n 4- divisao \n")

    if operacao == '1':
        res = soma(valor1,valor2)
        print(res)
        
    elif operacao == '2':
        res = sub(valor1, valor2)
        print(res)
    
    elif operacao == '3':
        res = multi(valor1, valor2)
        print(res)
        
    else:
         res = div(valor1, valor2)
    print(res)
    
if __name__ == "__main__":
    main()

#exit()        
#def main():
 #  x = 10
    #y = 15 

   #resultado = soma(x,y)
   #print (resultado)
   #print (soma(987, 512))
   #rint (sub(x,y))
   
