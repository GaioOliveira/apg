"""
Crie um programa em Python que peça ao usuário os dados de uma máquina do
laboratório:
● Modelo do Processador (ex: Ryzen 5)
● Quantidade de memória RAM
● Capacidade de Armazenamento em GB (ex: 512)
● Se o armazenamento é SSD (True ou False)
No final, exiba uma mensagem formatada com todas essas informações do computador.
"""

print("Ficha Técnica de PC do Laboratório 5")

cpu = input("Informe o modelo do processador:")
ram = input("Quantidade de memória RAM:")
armazenamento = input("Capacidade de armazenamento (memória secundária):")
ssd = input("Informe true para SSD ou false para HD:")

print(f"Modelo de CPU {cpu}")
print(f"Memória RAM --> {ram} GB")

if ssd=="true":
    print ("Armazenamento em SSD --> {armazenamento} ")
else:
    print ("Armazenamento em HD --> {armazenamento} ")
