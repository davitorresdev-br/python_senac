nome = input("Digite o seu nome: ")
livro = input("Digite o nome do livro que você deseja ler: ")
n_paginas = int(input("Digite a quantidade de páginas do livro: "))
tempo = int(input("Digite quanto tempo você costuma demorar para ler uma página: "))

# Inicio do código

estimativa = n_paginas * tempo
estimativa_horas = estimativa / 120

print(f'{nome}, você finalizará a leitura do livro {livro} em aproximadamente {estimativa_horas:.2f} horas.')