boletim = {
            "nome":"Fulano",
            "notas":[8.0,9.0,8.5],
}
soma = 0
print(boletim)

print(f"Notas do/da estudante {boletim['nome']} no 3º Bimestre:")
for nota in boletim['notas']:
    print(nota,end="| ")
    soma = soma + nota

media = soma/len(boletim['notas'])
print(f"\nMédia no 3º Bimestre: {media:.2f}")
   
# Será que dá para ter uma lista de dicionários?


boletins = []

n = int(input("Quantos estudantes? -->"))
for i in range(n):
    boletim = {}
    boletim['nome'] = input(f"Nome do/da estudante {i + 1}: ")
    boletim['Atividade1'] = float(input("Nota na Atividade 1:"))  
    boletim['Atividade2'] = float(input("Nota na Atividade 2:"))
    boletim['Atividade3'] = float(input("Nota na Atividade 3:"))
    boletins.append(boletim)
print("-"*10)

for b in boletins:
    for chave,valor in b.items():
        print(f"{chave.capitalize()}: {valor} ")
