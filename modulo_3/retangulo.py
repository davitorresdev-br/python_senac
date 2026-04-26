baseDoRetangulo = int(input("Digite a base do retângulo: "))
alturaDoRetangulo = int(input("Digite a altura do retângulo: "))

if baseDoRetangulo <= 0 or alturaDoRetangulo <= 0:
    print("Parâmetros inválidos.")
    exit()

retangulo = ""

for i in range(alturaDoRetangulo):
    for j in range(baseDoRetangulo):
        retangulo += "*"
    retangulo += "\n"
print(retangulo)