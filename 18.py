# coding: utf-8
print("- Velocidade de download - ")
tamanho = int(input("Tamanho do arquivo que vai ser baixado [MB]:\n > "))
velocidade = int(input("Velocidade da sua internet [Mbps]:\n > "))
tamanho=tamanho*8 #converter para megabits
tempoS=tamanho/velocidade
tempoM=tempoS/60
print(f"Vai demorar {tempoM:.2f} minutos para você concluir seu download.")