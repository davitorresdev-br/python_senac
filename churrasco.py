pessoas_presentes = int(input("Quantas pessoas virão ao churrasco? "))

# Preço por kg de cada tipo de carne
kg_carne = 50
kg_linguica = 28
kg_frango = 22

# Consumo individual de cada tipo de carne, em gramas
consumo_individual_carne = 300
consumo_individual_linguica = 200
consumo_individual_frango = 150

# Quantidade total de carnes necessárias para cada tipo, em kg
quantidade_carne = (pessoas_presentes * consumo_individual_carne) / 1000
quantidade_linguaca = (pessoas_presentes * consumo_individual_linguica) / 1000
quantidade_frango = (pessoas_presentes * consumo_individual_frango) / 1000

# Custo total para cada tipo de carne, considerando o preço por kg
preco_carne = quantidade_carne * kg_carne
preco_linguica = quantidade_linguaca * kg_linguica
preco_frango = quantidade_frango * kg_frango

preco_total = preco_carne + preco_linguica + preco_frango

# Custo para cada pessoa, considerando o preço por kg de cada tipo de carne
custo_per_pessoa = preco_total / pessoas_presentes 

print(f"Quantidades: Carne: {quantidade_carne:.2f} kg, Linguiça: {quantidade_linguaca:.2f} kg, Frango: {quantidade_frango:.2f} kg")

print(f"Custo total: Carne R$ {preco_carne:.2f}, Linguiça R$ {preco_linguica:.2f}, Frango R$ {preco_frango:.2f}")

print(f"Custo total do churrasco: R$ {preco_total:.2f}")

print(f"Cada pessoa deve contribuir com: R$ {custo_per_pessoa:.2f}")