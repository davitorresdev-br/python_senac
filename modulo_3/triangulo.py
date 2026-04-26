baseTriangulo = int(input("Digite a base do triângulo: "))

if baseTriangulo <= 0:
    print("Parâmetro inválido.")
    exit()

triangulo = ""

for i in range(1, baseTriangulo + 1):
    for j in range(i):
        triangulo += "*"
    triangulo += "\n"

print(triangulo)