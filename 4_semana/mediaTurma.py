# INICIALIZAÇÃO DE VARIÁVEIS
nota = 0
cont = 0
soma = 0

# LAÇO PARA ENTRADA DAS NOTAS DIFERENTE DE -1
while nota != -1:
    nota = float(input("Digite a nota do estudante:"))
    if nota != -1:
        # ACUMULADOR DE SOMA DAS NOTAS
        soma = nota + soma 
        # CONTADOR DE NOTAS
        cont = cont + 1
media = soma/cont
print(f"Média da turma: {media:.1f} pontos")