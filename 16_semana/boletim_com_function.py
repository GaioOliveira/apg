# DEFINIÇÃO DA FUNÇÃO PARA CALCULAR A MÉDIA
def calcular_media_estudante(boletim):
    """Recebe o boletim (dicionário) de um estudante 
    com a chave 'notas' e retorna a média."""
    lista_notas = boletim["notas"]
    media = sum(lista_notas)/len(lista_notas)
    return media

# TRECHO PRINCIPAL DO SCRIPT
# SUGESTÃO DA ESTRUTURA DO BOLETIM (DICIONÁRIO)
"""estudante_dic = {
    "prontuario": None,
    "nome":None,
    "notas":[]
    }
"""
lista_estudante = []

tamanho_turma = int(input("Quantos estudantes?:"))
quant_atividades = int(input("Quantas atividades avaliativas?:"))
for e in range(tamanho_turma):
    estudante_dic= {}
    estudante_dic["prontuario"] = input("Informe o prontuário do estudante:")
    estudante_dic["nome"] = input("Informe o nome do estudante:")
    estudante_dic["notas"]=[]
    for i in range(quant_atividades):
        estudante_dic["notas"].append(float(input(f"Informe a {i+1}ª nota:")))
    lista_estudante.append(estudante_dic)
print(lista_estudante)
