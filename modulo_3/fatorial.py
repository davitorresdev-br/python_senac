num = int(input("Digite um número para calcular o fatorial: "))

if num < 0:
    print("Parâmetro inválido.")

result = 0
n = int(num)

while n > 0:
    if result == 0:
        result = n
    else:
        result *= n
    n -= 1

print(f'O fatorial de {num} é {result}.')
