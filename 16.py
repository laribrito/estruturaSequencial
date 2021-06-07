# coding: utf-8
print("- Loja de tintas - ")
aTotal = float(input("Tamanho, em metros quadrados, da área a ser pintada:\n > "))
#1 litro de tinta para 3 m²
#vende-se latas com 18 L
#cada uma custa R$ 80,00
#informar a quantidade e o preço
lNecess=aTotal/3
latasNecess=lNecess/18
latasNecess=round(latasNecess + 0.5)
precoFinal=latasNecess*80

print(f"""
- Quantidade de latas : {latasNecess} latas;
- Preço final         : R$ {precoFinal:.2f}
""")