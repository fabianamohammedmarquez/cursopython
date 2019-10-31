frutas = {'banana':1.50, 'morango':3.00,'melancia':5.00}
cesta = []
 
print('Escolha suas frutas')


while True:
    menu = int(input('1-Banana\n 2-morango\n 3-melancia\n 4-sair\n '))
    if menu == 1:
       cesta.append(frutas['banana'])
    elif menu == 2:
        cesta.append(frutas['morango'])
    elif menu == 3:
        cesta.append(frutas['melancia'])
    elif menu == 4:
        break
    else:
        print('opcao invalida')
         
print(cesta)

soma = 0
for valor in cesta:
   soma = soma + valor

print ('O total de compras foi: R$',soma)

