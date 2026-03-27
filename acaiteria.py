qnt_acai_p = int(input('Quantos açaís pequenos você deseja: '))
qnt_acai_m = int(input('Quantos açaís médios você deseja: '))
qnt_acai_g = int(input('Quantos açaís grandes você deseja: '))
cupom_desconto = int(input("Qual o valor do seu cupom de desconto: "))

acai_p = 13.50
acai_m = 15.00
acai_g = 17.50

valor_p = qnt_acai_p * acai_p
valor_m = qnt_acai_m * acai_p
valor_g = qnt_acai_g * acai_g
valor_compra = valor_g + valor_m + valor_p

desconto = cupom_desconto / 100
desconto_aplicado = valor_compra * desconto
compra_aplicada = valor_compra - desconto_aplicado

print(f'Seu pedido foi registrado. \n-Açaí P: {qnt_acai_p} \n-Açaí M: {qnt_acai_m} \n-Açaí G: {qnt_acai_g} \n\nDesconto de {cupom_desconto}% aplicado. \nTotal R${compra_aplicada}')