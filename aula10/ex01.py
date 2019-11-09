from functools import reduce


#list comprehension
print('List Compre')
lista = [0,1,2,3,4,5,6,7,8,9,10]

nova_lista = [ x for x in lista if x %2!= 0]

print(lista)
print(nova_lista)


## Funcoes anonimas
print('Funcoes anonimas')
quadrado = lambda x: x**2

print(quadrado(2))


##filter
print('FIlter')

multiplo_2 = lambda x: x%2 == 0 

nova_lista = list(filter(multiplo_2,lista))
print(nova_lista)


#MAP

print('Map')

nova_lista = list(map(lambda x: x*2, lista))
print(nova_lista)


#REDUCE
lista = [1,1,1,1,1]
total = reduce(lambda x,y: x+y, lista)
print(total)

#é o msm que isso aqui ---> (((((1+)+1)+1)+1)+1)



