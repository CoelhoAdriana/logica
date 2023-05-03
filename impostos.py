total = input("Por favor, informe o valor total da manutenção do veículo: R$")
total = float(total)
iss = input("Agora, informe a alíquota do imposto sobre serviços, em %: ")
iss = float(iss) * total / 100
ipi = input("Finalmente, informe a alíquota do imposto sobre produtos industrializados, em %: ")
ipi = float(ipi) * total / 100
format_iss = "{:.2f}".format(iss)
format_ipi = "{:.2f}".format(ipi)
format_total ="{:.2f}".format(total - iss - ipi)
print("Os impostos devidos nessa transação são R$", format_iss, " e R$", format_ipi, ", com saldo final de R$", format_total , ".")