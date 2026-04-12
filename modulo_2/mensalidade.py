cursos_siglas = ["SI", "ADS", "CS", "EC", "ES"]
cursos_nomes = ["Sistemas de Informação", "Análise e Desenvolvimento de Sistemas", "Ciência da Computação", "Engenharia de Computação", "Engenharia de Software"]
mensalidade = [900, 750, 1150, 1300, 950]

for sigla, nome in zip(cursos_siglas, cursos_nomes):
    print(f"{sigla} - {nome}")

curso = input("Digite a sigla do curso do aluno: ")

if curso not in cursos_siglas:
    print("Curso inválido.")
else: 
    isento = input("O aluno é isento? (S/N): ")
    isento = isento.upper() != "N"
    desconto = int(input("Digite o valor em porcentagem do desconto (0-100)%: "))

    if desconto < 0:
        print("Valor de desconto inválido.")
    elif curso in cursos_siglas:
        index = cursos_siglas.index(curso)
        valor_mensalidade = mensalidade[index]

        if isento:
            print("O aluno é isento, portanto não precisa pagar a mensalidade.")
        else:
            valor_final = valor_mensalidade * (desconto / 100)
            if valor_final < 0:
                print("Valor final da mensalidade inválido. O desconto não pode ser maior que o valor da mensalidade.")
            else:
                print(f"O valor final da mensalidade para o curso {cursos_nomes[index]} é: R$ {valor_final:.2f}")