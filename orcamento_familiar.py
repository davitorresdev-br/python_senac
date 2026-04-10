ganhos = float(input("Informe o orçamento familiar mensal: "))
gastos = float(input("Informe os gastos mensais: "))

saldo_final_mes = ganhos - gastos
if ganhos >= gastos:
    print(f"Seu saldo no final do mês é de R${saldo_final_mes:.2f}. Ou seja, você está dentro do orçamento!")
else:
    print(f"Seu saldo no final do mês é de R${saldo_final_mes:.2f}. Ou seja, você está fora do orçamento! Não gaste mais.")