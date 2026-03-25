nome = input("Digite seu nome: ")
valor_compra = float(input("Digite o valor da sua compra: "))
cupom_desconto = int(input("Digite o valor do seu cupom: "))
desconto = cupom_desconto / 100
desconto_aplicado = valor_compra * desconto

compra_aplicada = valor_compra - desconto_aplicado

print(f'Olá {nome}, sua compra de R$ {valor_compra} foi confirmada! \nFoi aplicado um desconto de {cupom_desconto}%. \nO total final ficou em R$ {compra_aplicada}.')