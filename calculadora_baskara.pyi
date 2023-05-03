a = input("Por favor, informe o valor de 'a'. Lembre-se de utilizar um ponto para indicar casas decimais: ")
a = float(a)
b = input("Por favor, informe o valor de 'b': ")
b = float(b)
c = input("Por favor, informe o valor de 'c': ")
c = float(c)
vertice_x = (-1 * b) / (2 * a)
vertice_y = (-1 * b * b - 4 * a * c) / ( 2 * a)
print("A sua equação de segundo grau é ", a , "x² +", b , "x + ", c, ".")
print("Essa curva inclui os pontos (0, ", vertice_x, ") e (", vertice_y,", 0).")


