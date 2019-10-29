"""
idade = int(input("Digite sua idade: "))
hab = input("Possui Habilitaçao: ")

if (idade >= 18):
    if(hab == "sim"):
        print("Pode dirigir")
    else:
        print("Não possui habilitação")
else:
        print("Não possui idade minima")
"""

idade = int(input("Digite sua idade: "))
hab = input("Possui Habilitaçao: ")

if (idade >= 18 and hab == "sim"):
        print("Pode dirigir")
    else:
        print("Não possui habilitação")






exit()
#ex de media 

nota1 = float(input("Digite sua nota da P1: "))
nota2 = float(input("Digite sua nota da P2: "))
nota3 = float(input("Digite sua nota da Atividade: "))
resultado = (nota1+nota2+nota3)/3 

print("Calculando...")
print(resultado)


exit() 
#ex de soma
num1 = int(input("DIgite o primeiro numero: "))
num2 = int(input("Digite o segundo numero:  "))
resultado = num1+num2

print(resultado)


#script de saudaçao
exit()
nome = input("Digite seu nome:")
sobrenome = input("Digite seu sobrenome:")
print("Ola meu nome é", nome, sobrenome)
