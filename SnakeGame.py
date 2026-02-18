import turtle
import time
import random

# 1. INICIALIZACIÓN
retraso = 0.1
marcador = 0

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Snake Game en PYTHON")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0) # Movimientos sean fluidos

# 2. CREACIÓN DE OBJETOS

# Cabeza de la serpiente (snake_x, snake_y)
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup() # Para que no dibuje una línea al moverse
cabeza.goto(0,0)
cabeza.direction = "stop" # Estado inicial

# Comida (food_x, food_y)
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# 3. FUNCIONES DE MOVIMIENTO

def arriba():
    if cabeza.direction != "down": # Evita que se muerda el cuello
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# 4. TECLADO
ventana.listen()
ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(izquierda, "a")
ventana.onkeypress(derecha, "d")

# 5. BUCLE PRINCIPAL
while True:
    ventana.update()

    # A. Colisión con Bordes
    # 290 y -290 son los límites de una ventana de 600x600
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        marcador = 0 # Reiniciar puntuación
        print(f"Game Over. Puntuación: {marcador}")

    # B. Colisión con Comida
    if cabeza.distance(comida) < 20:
        # Mover la comida a un lugar aleatorio
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)
        marcador += 1
        print(f"¡Comiste! Puntuación: {marcador}")

    mover()
    time.sleep(retraso)