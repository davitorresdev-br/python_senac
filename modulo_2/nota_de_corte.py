nota_de_corte = int(input("Digite a nota de corte: "))
nota_minima = int(input("Digite a nota mínima: "))
nota_minima_aprovacao = int(input("Digite a nota mínima para aprovação: "))

if nota_de_corte < 0 or nota_minima < 0 or nota_minima_aprovacao < 0:
    print("Notas inválidas. As notas devem ser maiores ou iguais a zero.")

if nota_de_corte > 10 or nota_minima > 10 or nota_minima_aprovacao > 10:
    print("Notas inválidas. As notas devem ser menores ou iguais a 10.")

if nota_de_corte >= nota_minima_aprovacao:
    print("Reprovado por nota de corte")
elif nota_minima_aprovacao > nota_de_corte >= nota_minima:
    print("Lista de espera")
elif nota_de_corte < nota_minima:
    print("Aprovado")