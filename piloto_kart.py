tamanho_pista = int(input("Qual o tamanho da pista em metros: "))
qnt_voltas = int(input('Quantas voltas são necessárias para concluir o percurso: '))
tempo_primeira_volta = int(input('Quanto tempo você demorou para concluir a primeira volta em segundos: '))

distancia_total = tamanho_pista * qnt_voltas / 1000
previsao_conclusao = (tempo_primeira_volta * qnt_voltas) / 60

print(f'Análise Preditiva Concluída \n--\nDistância total a ser percorrida: {distancia_total}km. \nPrevisão de conclusão: {previsao_conclusao:.1f} minutos.')