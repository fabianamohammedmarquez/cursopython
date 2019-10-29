valor1 = float(input("Digite o valor: "))
valor2 = float(input("Digite um segundo valor: "))
operacao = input("o que deseja realizar: ")

if (operacao == "+"):
    print(valor1+valor2)
elif (operacao == "-"):
    print(valor1-valor2)
elif (operacao == "*"):
    print(valor1*valor2)
elif (operacao == "/"):
    print(valor1/valor2)
elif (operacao == "%"):
    print(valor1%valor2)
elif (operacao == "**"):
    print(valor1**valor2)
else:
    print("opcao invalida")
