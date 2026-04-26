total_compras = 0.0

while True:
    valor_item = float(input('Digite o valor da compra (0 para finalizar): '))

    if valor_item == 0:
        break

    if valor_item < 0:
        print('Valor inválido.')
        continue

    total_compras += valor_item

parcelas = int(input('Digite o número de parcelas: '))

if parcelas <= 1:
    print(f'Valor total a pagar: R$ {total_compras:.2f}')
else:
    valor_parcela = total_compras / parcelas
    print(f'Valor total da compra: R$ {total_compras:.2f}')
    print(f'Parcelado em {parcelas}x de R$ {valor_parcela:.2f}')
