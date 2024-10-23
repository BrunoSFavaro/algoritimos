pg = float(input("Quanto você ganha por hora? "))
hora = float(input("Quantas horas você trabalha por mês? "))

bruto = pg * hora
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
desconto = ir + inss + sind
liq = bruto - desconto

print(f"+ Salário Bruto: R${bruto}")
print(f"- IR (11%): R${ir}")
print(f"- INSS (8%): R${inss}")
print(f"- Sindicato (5%): R${sind}")
print(f"= Salário Líquido: R${liq}")