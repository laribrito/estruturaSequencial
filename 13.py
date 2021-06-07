# coding: utf-8
print("- 'Peso ideal' - ")
al = float(input("Qual a sua altura [em metros] ?:\n > "))
forM = (72.7*al) - 58
print(f"Se for um homem, seu peso ideal é {forM} kg.")
forW = (62.1*al) - 44.7
print(f"Sendo mulher, é esse: {forW}. kg")
