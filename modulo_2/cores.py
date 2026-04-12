primary_colors = ["vermelho", "verde", "azul"]

color1 = input("Informe a primeira cor primária: ")
color2 = input("Informe a segunda cor primária: ")

if color1 in primary_colors and color2 in primary_colors:
    if color1 == "vermelho" and color2 == "verde" or color1 == "verde" and color2 == "vermelho":
        print("A mistura de vermelho e verde resulta em amarelo.")
    elif color1 == "vermelho" and color2 == "azul" or color1 == "azul" and color2 == "vermelho":
        print("A mistura de vermelho e azul resulta em roxo.")
    elif color1 == "verde" and color2 == "azul" or color1:
        print("A mistura de verde e azul resulta em ciano.")
else:
    print(f"Apenas as cores primárias são aceitas: {', '.join(primary_colors)}")