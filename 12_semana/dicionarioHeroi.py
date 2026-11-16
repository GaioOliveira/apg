heroi = {
    "codinome":"Homem-Aranha",
    "nome_real":"Peter Parker",
    "idade": 18,
    "cidade":"Nova York",
    "forca": 95
}
print(f"Codinome: {heroi["codinome"]}")
print(f"Força: {heroi["forca"]}")

heroi["altura"] = 1.7
print(f"Altura: {heroi.get("altura")} m")

# Alterando a força
heroi["forca"] = 100
print("Exibindo o herói com força alterada...\n")
print(f"Codinome: {heroi.get("codinome")}")
print(f"Força: {heroi.get("forca")}")

# Dicionário com todas as chaves e valores
print ("\nTodos os dados do herói...\n")
print(heroi)
# Comando para excluir uma chave (e o valor)
del heroi["altura"]
print ("\nDados do herói (altura removida)...\n")
print(heroi)

