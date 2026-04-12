week_day_name = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
    ]

day_number = int(input("Digite um número: "))
if 0 <= day_number < len(week_day_name):
    print(week_day_name[day_number])
else:
    print("Dia da semana inválido.")
