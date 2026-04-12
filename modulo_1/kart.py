# Entrada de dados
tamanho_pista = float(input("Digite o tamanho da pista (em metros): "))
voltas = int(input("Digite a quantidade de voltas: "))
tempo_volta = float(input("Digite o tempo da primeira volta (em segundos): "))

# Cálculo da distância total (em km)
distancia_total_m = tamanho_pista * voltas
distancia_total_km = distancia_total_m / 1000

# Previsão de tempo total (em minutos)
tempo_total_segundos = tempo_volta * voltas
tempo_total_minutos = tempo_total_segundos / 60

# Saída
print("\n--- RESULTADOS ---")
print(f"Distância total da corrida: {distancia_total_km:.2f} km")
print(f"Tempo estimado para concluir a corrida: {tempo_total_minutos:.1f} minutos")