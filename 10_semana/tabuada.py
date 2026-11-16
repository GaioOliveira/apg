# ENTRADA DE DADOS
num = int(input("Tabuada de qual número? -->"))
# LAÇO for PARA CALCULAR A TABUADA DE num
for cont in range(1,11):
    # CÁLCULO DA TABUADA MULTIPLICANDO O num PELO contador
    resultado = num * cont
    # IMPRIMINDO CADA RESULTADO DA TABUADA 
    print (f"{num} x {cont:2d} = {resultado:2d}")
    """ O parâmetro ":2d" serve para alinhar número de até 
    2 dígitos """