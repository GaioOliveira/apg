"""
Escreva um script em Python que solicite continuamente
a idade e a nota do filme (de 1 a 5) de
cada espectador.O laço (while) deve ser encerrado
assim que for digitada uma idade igual a 0.

Dentro do laço, utilize contadores e a
estrutura if para:
Contar a quantidade de avaliações altas
(notas 4 e 5) e de avaliações mais baixas
(notas 1, 2 e 3).
Acumular a soma das idades dos espectadores
para posterior cálculo de média.
"""

idade = int(input("Informe a sua idade:"))
nota = int(input("Dê uma nota para o filme (de 1 a 5):"))

contaAltas = 0
contaBaixas = 0
somaIdades = 0

while (idade != 0):
    if (nota >= 4 and nota <=5):
        contaAltas = contaAltas + 1
    elif (nota >= 1 and nota <=3):
        contaBaixas = contaBaixas + 1
    else:
        print("Nota inválida! Valores de 1 a 5")
    somaIdades = somaIdades + idade
    idade = int(input("Informe a sua idade:"))
    if idade != 0: 
        nota = int(input("Dê uma nota para o filme (de 1 a 5):"))


conTotal = contaBaixas + contaAltas
if conTotal > 0:
    mediaIdade = somaIdades/conTotal
    print(f"Total de avaliações --> {conTotal}")
    print(f"Total de avaliações altas: {contaAltas}")
    print(f"Total de avaliações baixas: {contaBaixas}")
    print(f"Média das idades dos avaliadores: {mediaIdade}")
    

