
frutas = ['banana', 'morango','melancia']
cesta = []
 
print('Escolha suas frutas')


while True:
    menu = int(input('1-Banana\n 2-morango\n 3-melancia\n 4-sair\n '))
    if menu == 1:
       cesta.append(frutas[0])
    elif menu == 2:
        cesta.append(frutas[1])
    elif menu == 3:
        cesta.append(frutas[2])
    elif menu == 4:
        break
    else:
        print("opcao invalida")
            
print(cesta)
