import turtle
# CONFIGURAÇÕES DA TELA
tela = turtle.Screen()
caneta = turtle.Turtle()
tela.setup(800,600)
tela.title("Exercício 3 da Semana 6")
tela.bgcolor("#252525")

# CONFIGURAÇÕES DA CANETA
caneta.color("#eeeeee","#eeeeee")

# DESENHANDO COM POLÍGONOS

# Tamanho do passo 
passo = 70


# Iniciando contador, abaixando a caneta
cont = 0
caneta.pendown()


caneta.begin_fill()
while cont < 4:
    caneta.forward(passo)
    caneta.left(90)
    cont = cont + 1
caneta.end_fill()


cont = 0
caneta.penup()
caneta.goto(-70,0)
caneta.pendown()
caneta.begin_fill()
while cont < 4:
    caneta.forward(passo)
    caneta.left(90)
    cont = cont + 1
caneta.end_fill()

cont = 0
caneta.penup()
caneta.goto(-70,70)
caneta.pendown()
caneta.pensize(2)
caneta.color("#ff0000")
caneta.begin_fill()
caneta.forward(passo*2)
caneta.left(135)
caneta.forward(passo*1.4)
caneta.left(90)
caneta.forward(passo*1.4)
caneta.left(135)
caneta.forward(passo) 
caneta.end_fill()



tela.exitonclick()