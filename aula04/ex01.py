#!usr/bin/python3



def soma (*numeros):
    print(numeros)
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado
    
    
def main():
    #umeros = [2,4,6,8))
    print(soma(2,4,6,8))
if __name__ == "__main__":
    main()
