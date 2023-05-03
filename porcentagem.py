total = input("Por favor, informe o número total de balas contadas no pacote: ")
total = int(total)
morango = input("Agora, informe o número de balas cujo sabor era morango: ")
morango = 100 * int(morango) / total
limao = input("Finalmente, informe o número de balas sabor limão: ")
limao = 100 * int(limao) / total
format_limao = "{:.1f}".format(limao)
format_morango = "{:.1f}".format(morango)
laranja = 100 - morango - limao
format_laranja = "{:.1f}".format(laranja)
print("Nesse pacote de balas, ", format_limao , "% das balas eram de limão, ", format_morango , "% eram de morango e ", laranja, "% eram balas de laranja.")