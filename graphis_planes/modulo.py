import turtle
import math
class Figura:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(2)
        self.screen = turtle.Screen()

    def dibujar_cuadrado(self, ancho, alto):
        for _ in range(2):
            self.t.forward(ancho)
            self.t.right(90)
            self.t.forward(alto)
            self.t.right(90)


    def dibujar_triangulo(self, base, altura):
    # Calcular la longitud de los otros dos lados usando la fórmula del triángulo rectángulo
         lado = math.sqrt((base / 2) ** 2 + altura ** 2)

    # Calcular el ángulo en la base
         angulo_base = math.degrees(math.atan(altura / (base / 2)))

    # Dibujar el triángulo
         self.t.forward(base)       # Dibujar la base
         self.t.left(180 - angulo_base) # Girar para dibujar el primer lado
         self.t.forward(lado)       # Dibujar el primer lado
         self.t.left(2 * angulo_base)   # Girar para dibujar el segundo lado
         self.t.forward(lado)       # Dibujar el segundo lado
         self.t.left(180 - angulo_base) # Regresar a la posición original

    def mover_a_posicion(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def finalizar_dibujo(self):
        """Finaliza el dibujo y cierra la ventana de Turtle."""
        turtle.done()

if __name__ == "__main__":
    figura = Figura()
    figura.dibujar_cuadrado(200, 300)
    figura.mover_a_posicion(200, 50)
    figura.dibujar_triangulo(400, 200)
    
    figura.finalizar_dibujo()