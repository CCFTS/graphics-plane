import turtle

class Figura:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(1)
        self.screen = turtle.Screen()
 

    def dibujar_cuadrado(self, lado):
        
        for _ in range(4):
            self.t.forward(lado)
            self.t.right(90)

    def dibujar_triangulo(self, lado):
      
        for _ in range(3):
            self.t.forward(lado)
            self.t.right(120)

    def mover_a_posicion(self, x, y):
    
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def finalizar_dibujo(self):
        """Finaliza el dibujo y cierra la ventana de Turtle."""
        turtle.done()
    
    
if __name__ == "__main__":
    figura = Figura()
    figura.dibujar_cuadrado(200)
    figura.mover_a_posicion(300, 0)
    figura.dibujar_triangulo(200)

    figura.finalizar_dibujo()

    
    
    


    
