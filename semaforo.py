semaforo = input("Informa a cor do semáforo no atual momento: ")

if semaforo == "verde":
    print("Atravesse")
elif semaforo == "vermelho":
    print("Espere")
else:
    print("Cor inválida. Informe 'verde' ou 'vermelho'.")