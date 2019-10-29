data = int(input("Informe o ano de nascimento: "))

if (data <= 1964):
    print("Voce é um Boomer")
elif (data <=1981 >= 1964):
    print("Voce é da geração X")
elif (data <=1996 >= 1981):
    print("Voce é da geração Y")
elif (data <=2019 >= 1996):
    print("Voce é da geração Z")

#outro jeito
if data < 1965:
    print("Geração Boomer")
elif data < 1981:
    print("Geração X")
elif data <1996:
    print("Geração Y")
else:
    print("geraçao Z")
