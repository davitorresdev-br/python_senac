palavra_original = input('Digite uma palavra: ')
palavra_soletrada = ''

print('Informe as letras da palavra uma a uma. Digite 0 para finalizar.')

while True:
    letra = input('Letra: ')
    if letra == '0':
        break
    elif letra == '':
        print('Entrada inválida. Digite uma letra ou 0 para sair.')
        continue
    palavra_soletrada += letra

print(f'Palavra original: {palavra_original}')
print(f'Palavra soletrada: {palavra_soletrada}')
