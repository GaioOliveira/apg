# ENTRADAS
la = int(input("Informe a medida (cm) do lado A:")) 
lb = int(input("Informe a medida (cm) do lado B:")) 
lc = int(input("Informe a medida (cm) do lado C:"))
# VALIDAÇÃO DAS MEDIDAS COMO LADOS DE TRIÂNGULO
if la+lb > lc and la+lc > lb and lb+lc > la:
    print("Medidas válidas para um triângulo!")
    if la == lb and lb == lc:
        print("É um triângulo equilátero.")
    elif la != lb and lb != lc:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo isósceles.")
else:
    print("Medidas NÃO válidas para um triângulo!")