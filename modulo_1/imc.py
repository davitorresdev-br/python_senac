nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = int(input("Digite o seu peso: "))
imc = peso / (altura ** 2)  # IMC = peso / (altura ** 2)

print(f'{nome}, seu IMC é de {imc:.4f}')
