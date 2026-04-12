absences = int(input("Digite o número de faltas do aluno: "))

if absences < 0:
    print("Número de faltas inválido.")
    
if absences > 4:
    print("Reprovado por Falta")

else:
    grade1 = float(input("Digite a primeira nota do aluno: "))
    grade2 = float(input("Digite a segunda nota do aluno: "))
    grade3 = float(input("Digite a terceira nota do aluno: "))
    grade4 = float(input("Digite a quarta nota do aluno: "))
    average = (grade1 + grade2 + grade3 + grade4) / 4

    if average < 0 or absences > 10:
        print("Parâmetros inválidos")

    if average >= 8 and average <= 10 and absences <= 4:
        print(f"Aprovado com sucesso! Média: {average:.2f} | Faltas: {absences}")

    if average >= 6 and average <= 8 and absences <= 4:
        print(f"Aprovado Média: {average:.2f} | Faltas: {absences}")

    if average < 6 and absences <= 4:
        print("Recuperação")

    if average == 0:
        print("Desistente")