metas = input("Digite quais são as suas metas (caso for mais de uma, para adicionar os itens na lista, utilize +): ")
valor_metas = float(input("Digite o valor das suas metas: "))
salario = float(input("Quanto você ganha por mês: "))
despesas = float(input("Quanto te custa as suas despesas mensalmente: "))

salario_pos_despesas = salario - despesas
reserva_fixa = salario_pos_despesas * 0.30
valor_disponivel_meta = salario_pos_despesas - reserva_fixa

meses = valor_metas / valor_disponivel_meta

print(f'Meta: {metas} (R${valor_metas:.2f})\nSalario: R${salario:.2f} - Despesas: R${despesas:.2f}\n\n')
      
print(f"Saldo apos despesas: R${salario_pos_despesas:.2f}\nReserva fixa(30%): R${reserva_fixa:.2f}\nValor disponivel para a meta: R$ {valor_disponivel_meta:.2f} por mês \nPrazo estimado para atingir a meta: {meses:.2f} meses")


