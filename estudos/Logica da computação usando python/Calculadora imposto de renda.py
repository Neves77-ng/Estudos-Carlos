salario_bruto = float(input("Informe o seu sálario:"))

aliquota = 0
parcela_deduzir = 0

if salario_bruto <= 2259.20:
    aliquota = 0
    parcela_deduzir = 0

elif salario_bruto <= 2826.65:
    aliquota = 0.075
    parcela_deduzir = 169.44

elif salario_bruto <= 3751.05:
    aliquota = 0.15
    parcela_deduzir = 381.44

elif salario_bruto <= 4664.68:
    aliquota = 0.225
    parcela_deduzir = 662.77

else:
    aliquota = 0.275
    parcela_deduzir = 896.00

imposto = salario_bruto * aliquota - parcela_deduzir
salario_liquido = salario_bruto - imposto

print(f"Salario bruto: {salario_bruto:.2f}")
print(f"Imposto de renda: {imposto:.2f}")
print(f"Salario liquido: {salario_liquido:.2f}")
