# coding: utf-8
print("- Salário - ")
porH = float(input("Quanto você ganha por hora?\n > "))
horas = int(input("Quantas horas você trabalha no mês?\n > "))
bruto=horas*porH
ir=bruto*(11/100)
inss=bruto*(8/100)
sind=bruto*(5/100)
liq=bruto-ir-inss-sind

print(f"""
+ Salário Bruto   : R$ {bruto}
- IR (11%)        : R$ {ir}
- INSS (8%)       : R$ {inss}
- Sindicato (5%) : R$ {sind}
= Salário Liquido : R$ {liq}
""")