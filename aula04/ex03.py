
cesta = []

def frutas (numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
 
 
def adiciona_item(valor):
    cesta.append(valor)
 
 
    
def soma (numeros):
    print(numeros)
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

def main():
    frutas = {'banana':1.50, 'morango':3.00,'melancia':5.00}
    menu = input('1-Banana\n 2-morango\n 3-melancia\n 4-sair\n ')
    
    if menu == '1':
        adiciona_item(frutas['banana'])
    
    elif menu == '2':
        adiciona_item(frutas['morango'])
    
    elif menu == '3':
        adiciona_item(frutas['melancia'])
        
    elif menu == '4':
         break
    else:
        print('opcao invalida')
    
    
    print(cesta)

if __name__ == "__main__":
    main()

