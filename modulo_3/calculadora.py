n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("\nSelecione qual operador você quer utilizar:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
opcao = int(input("\nDigite o número da operação desejada: "))

if opcao == 1:
    print(f'\n{n1} + {n2} = {n1 + n2}')
elif opcao == 2:
    print(f'\n{n1} - {n2} = {n1 - n2}')
elif opcao == 3:
    print(f'\n{n1} X {n2} = {n1 * n2}')
elif opcao == 4:
    if n2 == 0:
        print("\nErro: Divisão por zero não é permitida.")
    else:
        print(f'\n{n1} / {n2} = {n1 / n2}')
else:
    print("\nOpção inválida. Por favor, selecione uma opção entre 1 e 4.")