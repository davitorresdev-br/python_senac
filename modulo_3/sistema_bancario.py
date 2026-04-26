saldo = 0.0

while True:
    print('Menu de Opções')
    print('1. Consultar Saldo')
    print('2. Realizar Depósito')
    print('3. Realizar Saque')
    print('0. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '0':
        break
    elif opcao == '1':
        print(f'Saldo atual: R$ {saldo:.2f}')
    elif opcao == '2':
        valor = float(input('Digite o valor do depósito: '))
        if valor < 0:
            print('Valor inválido')
        else:
            saldo += valor
            print(f'Depósito realizado. Saldo atual: R$ {saldo:.2f}')
    elif opcao == '3':
        valor = float(input('Digite o valor do saque: '))
        if valor < 0:
            print('Valor inválido')
        elif valor > saldo:
            print('Saldo insuficiente')
        else:
            saldo -= valor
            print(f'Saque realizado. Saldo atual: R$ {saldo:.2f}')
    else:
        print('Opção inválida')

print('Programa encerrado.')
