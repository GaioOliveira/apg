import turtle
# CONFIGURAÇÕES DA TELA
tela = turtle.Screen()
caneta = turtle.Turtle()
tela.setup(800,600)
tela.title("Exercício 2 da Semana 6")
tela.bgcolor("#252525")

# CONFIGURAÇÕES DA CANETA
caneta.color("#eeeeee","#eeeeee")

# DESENHANDO OS POLÍGONOS

# Tamanho do passo e quantidade de vértices (lados) para cada polígono
passo = 70
triangulo = 3
quadrado = 4
pentagono = 5

# Iniciando contador, abaixando a caneta
cont = 0
caneta.pendown()

# LAÇO PARA FAZER O TRIÂNGULO
caneta.begin_fill()
while cont < triangulo:
    caneta.forward(passo)
    caneta.left(120)
    cont = cont + 1
caneta.end_fill()

# Levantando a caneta e mudando-a de lugar 
caneta.penup()
caneta.goto(-150,-150)

# Iniciando o contador novamente e abaixando a caneta (necessário para cada polígono)
cont = 0
caneta.pendown()
while cont < quadrado:
    caneta.forward(passo)
    caneta.left(90)
    cont = cont + 1

# Levantando a caneta e mudando-a de lugar 
caneta.penup()
caneta.goto(150,150) 

cont = 0
caneta.pendown()
while cont < pentagono:
    caneta.forward(passo)
    caneta.left(72)
    cont = cont + 1

tela.exitonclick()