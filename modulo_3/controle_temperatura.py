maior_temp = -100
menor_temp = 100
teve_temperatura_valida = False

while True:
    temp = float(input("Digite uma temperatura (0 para sair): "))

    if temp == 0:
        break

    if temp < -50 or temp > 60:
        print("Temperatura inválida")
        continue

    teve_temperatura_valida = True

    if temp > maior_temp:
        maior_temp = temp

    if temp < menor_temp:
        menor_temp = temp

if teve_temperatura_valida:
    print(f"Maior temperatura: {maior_temp:.1f}")
    print(f"Menor temperatura: {menor_temp:.1f}")