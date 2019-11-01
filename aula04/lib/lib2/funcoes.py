CONSTANTE =




def soma (*numeros):
    print(numeros)
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
    
def sub(*numeros):
    resultado = 0
    for num in numeros:
        resultado -= num
    return resultado
