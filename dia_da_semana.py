# Mapeamento de dias da semana com seus respectivos números
dias_da_semana = {
    "Domingo": 0,
    "Segunda": 1,
    "Terça": 2,
    "Quarta": 3,
    "Quinta": 4,
    "Sexta": 5,
    "Sábado": 6
}

# Função para obter o número do dia
def obter_numero_dia(dia):
    """Retorna o número correspondente ao dia da semana"""
    return dias_da_semana.get(dia, "Dia inválido")

# Função para obter o nome do dia pelo número
def obter_nome_dia(numero):
    """Retorna o nome do dia correspondente ao número"""
    for dia, num in dias_da_semana.items():
        if num == numero:
            return dia
    return "Número inválido"

# Exemplos de uso
if __name__ == "__main__":
    print("=== Dias da Semana ===\n")
    
    # Exibir todos os dias e seus números
    print("Mapeamento completo:")
    for dia, numero in dias_da_semana.items():
        print(f"{dia}: {numero}")
    
    print("\n" + "="*30 + "\n")
    
    # Entrada do usuário
    try:
        numero_digitado = int(input("Digite um número de 0 a 6 para descobrir o dia da semana: "))
        
        if numero_digitado < 0 or numero_digitado > 6:
            print("Dia da semana inválido")
        else:
            dia_correspondente = obter_nome_dia(numero_digitado)
            print(f"Número {numero_digitado} = {dia_correspondente}")
    
    except ValueError:
        print("Dia da semana inválido")
