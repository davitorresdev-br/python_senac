nome = input("Digite o seu nome: ")
nota1 = input("Quanto você tirou na P1: ")
nota2 = input("Quanto você tirou na P2: ")
nota3 = input("Quanto você tirou na P3: ")

floatnota1 = float(nota1)
floatnota2 = float(nota2)
floatnota3 = float(nota3)

soma = floatnota1 + floatnota2 + floatnota3
media = soma / 3

print(f"O(A) estudante {nome} ficou com média {media:.3f}")