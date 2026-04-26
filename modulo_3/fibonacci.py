numPosition = int(input("Digite um número para verificar se pertence à sequência de Fibonacci e sua posição: "))

lastNumber = 0
fibonacci = 1
nextNumber = 1
position = 1

a = ""

while True:

    a += f'{fibonacci} '

    if position == numPosition:
        print(f'O valor na posição {position} da sequência de Fibonacci é {fibonacci}.')
        print(a)
        break

    lastNumber = fibonacci
    fibonacci = nextNumber
    nextNumber = fibonacci + lastNumber

    position += 1