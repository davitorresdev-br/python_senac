maior_temp = -100
menor_temp = 100
teve_temperatura_valida = False

while True:
    try:
        temp = float(input("Digite a temperatura (ou 0 para encerrar): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue
    if temp == 0:
        break

    if temp < -50 or temp > 60:
        print("Temperatura inválida.")
        continue
    
    teve_temperatura_valida = True

    if temp > maior_temp:
        maior_temp = temp

    if temp < menor_temp:
        menor_temp = temp

if teve_temperatura_valida:
    print(f"\nMaior temperatura registrada: {maior_temp}°C")
    print(f"Menor temperatura registrada: {menor_temp}°C")
else:
    print("Nenhuma temperatura válida foi registrada.")