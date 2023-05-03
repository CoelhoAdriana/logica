var1 = input("Informe o valor dos rendimentos totais em um ano: R$")
var1 = float(var1)
result = var1 / 13
format_result = "{:.2f}".format(result)
print("Levando em consideração o 13º salário, a remuneração mensal deve ser R$ ", format_result, ".")