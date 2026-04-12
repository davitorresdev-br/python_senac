ingresso_cheio = 28.50
ingresso_meia = ingresso_cheio / 2
ingresso_quarta = 14.50
ingresso_nacional = 5.00

print("Bem-vindo ao cinema!")
qtd_inteiras = int(input("Digite a quantidade de ingressos inteiros: "))
qtd_meias = int(input("Digite a quantidade de ingressos meia-entrada: "))
dia_semana = input("Digite o dia da semana (por exemplo: segunda, quarta, sabado): ")
filme_nacional = input("O filme é nacional? (sim ou nao): ")

if filme_nacional == "sim":
    total = (qtd_inteiras + qtd_meias) * ingresso_nacional
elif dia_semana == "quarta":
    total = (qtd_inteiras + qtd_meias) * ingresso_quarta
else:
    total = qtd_inteiras * ingresso_cheio + qtd_meias * ingresso_meia

print(f"Total a pagar: R$ {total:.2f}")