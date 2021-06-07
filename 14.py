# coding: utf-8
print("- Vai seu João! - ")
kilo = float(input("Quantos quilos de peixe o sr. pescou hoje?\n > "))
if kilo >50:
    excesso=kilo-50
    multa=excesso*4
    print(f"Por ter passado {excesso} kg do limite da cidade, sua multa será de R$ {multa}.")
else:
    print(f"Você não passou do limite da cidade, fique tranquilo e vá descansar!")

