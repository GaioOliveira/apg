"""
1) Criar um script para que o usuário digite os valores
de uma lista de 10 números inteiros.
Imprimir na tela apenas os números ímpares da lista. 
"""
# CRIANDO UMA LISTA VAZIA
numeros = []

# LAÇO PARA PREENCHER A LISTA COM INTEIROS
for i in range(10):
    n = int(input("Digite um número inteiro:"))
    numeros.append(n)

# VERIFICANDO SE A LISTA FOI PREENCHIDA
print(numeros)

print ("***** Imprimindo os ímpares da lista *****")
# PERCORRENDO A LISTA ITEM POR ITEM
for n in range(10):
    # VERIFICANDO SE O ITEM DA LISTA DE ÍNDICE i
    # É ÍMPAR
    if numeros[i] % 2 != 0:
        print(numeros[i])
