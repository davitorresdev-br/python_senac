price_100g = 3.50

weight_to_buy = float(input("Digite a quantidade de gramas que deseja comprar: "))

if weight_to_buy <= 0:
    print("Peso Inválido.")

if weight_to_buy >= 1000:
    print("Desconto aplicado! O peso de 100g agora é R$ 0.50")
    price_100g = 0.50

total_price = (weight_to_buy / 100) * price_100g

if total_price > 0:
    print(f"O preço total é R$ {total_price:.2f}")