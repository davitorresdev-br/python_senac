numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /, %): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado:.2f}")

elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado:.2f}")

elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado:.2f}")

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operacao == "%":
    if numero2 != 0:
        resultado = numero1 % numero2
        print(f"O resultado do módulo é: {resultado:.2f}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação válida (+, -, *, /, %).")