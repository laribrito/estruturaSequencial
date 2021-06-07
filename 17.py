# coding: utf-8
print("- Loja de tintas - ")
aTotal = float(input("Tamanho, em metros quadrados, da área a ser pintada:\n > "))
#1 litro de tinta para 6 m²
#vende-se latas com 18 L, que custam R$ 80,00
#vende-se galões de 3,6 L, que custam R$ 25,00
#informar a quantidade e o preço
lNecess=(aTotal//6)+1
#somente latas
latasNecess=(lNecess//18)+1
precoLatas=latasNecess*80
#somente galões
galoesNecess=(lNecess//3.6)+1
precoGaloes=galoesNecess*25
#misto
MlatasNecess=lNecess//18
MgaloesNecess=((lNecess%18)//3.6)+1
precoM=(MlatasNecess*80)+(MgaloesNecess*25)
print(f"""
Só latas
- Quantidade de latas : {latasNecess} latas;
- Preço final         : R$ {precoLatas:.2f}
""")
print(f"""
Só galões
- Quantidade de galões : {galoesNecess} galões;
- Preço final         : R$ {precoGaloes:.2f}
""")
print(f"""
Misto
- Quantidade de latas : {MlatasNecess} latas;
- Quantidade de galões : {MgaloesNecess} galões;
- Preço final         : R$ {precoM:.2f}
""")