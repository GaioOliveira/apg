# CRIAÇÃO DE LISTA DE ESTUDANTES
estudantes = ["Ana","Bruno","Carla","Daniel, gaio"]
print("")
print("Lista de estudantes")
#EXIBINDO NA TELA A LISTA TODA
print(estudantes)

#EXIBINDO UM ITEM ESPECÍFICO DA LISTA
print(f"{estudantes[2]} é a/o terceira(o) estudante da lista")

#EXIBINDO A QUANTIDADE DE ITENS  NA LISTA
print(f"A lista possui {len(estudantes)} estudantes")

# ADICIONANDO NOVOS ESTUDANTE NA POSIÇÃO (ÍNDECE) 2 DA LISTA
print(f"Substituindo o estudante de índice 2")
estudantes[2] = "fernanda"

print(estudantes)

#ADICINANDO UM NOVO ESTUDANTE AO FINAL DA LISTA
estudantes.append("Eduardo")
print("Novo estudante adicionado")
print(estudantes)

print(f"A lista possui AGORA {len(estudantes)} estudantes")


#REMOVENDO O ESTUDANTE Bruno DA LISTA
print("REMOVENDO O ESTUDANTE Bruno DA LISTA")
estudantes.remove("bruno")

print(estudantes)

#REMOVENDO O ESTUDANTE Bruno DA LISTA
print("REMOVENDO O ESTUDANTE de índece 4 DA LISTA")
estudantes.pop(4)

print(estudantes)