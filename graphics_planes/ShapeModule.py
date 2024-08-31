import math
import svgwrite

class Shape:
    def __init__(self, width, height, label, x=0, y=0):
        self.width = width
        self.height = height
        self.label = label
        self.x = x*-1
        self.y = y*-1

    def draw(self, drawer):
        raise NotImplementedError("Subclasses should implement this method.")

    def export_to_svg(self, drawer, file_name):
        dwg = svgwrite.Drawing(file_name, profile='tiny')
        shape_group = dwg.add(dwg.g(id='shape', fill='none', stroke='black'))
        self._draw_to_svg(shape_group, drawer)
        dwg.save()

    def _draw_to_svg(self, shape_group, drawer):
        raise NotImplementedError("Subclasses should implement this method for SVG export.")
    
class Rectangle(Shape):
    def draw(self, drawer):
        x = self.width
        y = self.height
        ob = drawer

        def draw_part():
            center_x = x / 2
            center_y = y / 2

            ob.penup()
            ob.goto(self.x - center_x, self.y + center_y)
            ob.pendown()

            for _ in range(2):
                ob.forward(x)
                ob.write(f"{x} cm", align="center", font=("Arial", 12, "normal"))
                ob.right(90)
                ob.forward(y)
                ob.right(90)
                ob.write(f"{y} cm", align="center", font=("Arial", 12, "normal"))

            ob.penup()
            ob.goto(self.x, self.y)
            ob.pendown()
            ob.write(self.label, align="center", font=("Arial", 16, "normal"))

        draw_part()

    def _draw_to_svg(self, shape_group, drawer):
        x = self.width
        y = self.height

        # Ajustar la posición para centrar el rectángulo en (self.x, self.y)
        insert_x = self.x - x / 2
        insert_y = self.y - y / 2

        # Añadir el rectángulo al SVG con la posición ajustada
        shape_group.add(drawer.rect(insert=(insert_x, insert_y), size=(x, y)))

        # Añadir la etiqueta en el centro
        shape_group.add(drawer.text(self.label, insert=(self.x, self.y), text_anchor="middle"))

class Triangle(Shape):
    def draw(self, drawer):
        base_length = self.width 
        triangle_height = self.height 
        ob = drawer

        side_length = math.sqrt((base_length / 2) ** 2 + triangle_height ** 2)
        angle_base = math.degrees(math.atan(triangle_height / (base_length / 2)))

        def draw_part():
            ob.forward(base_length)
            ob.left(180 - angle_base)
            ob.forward(side_length)
            ob.left(2 * angle_base)
            ob.forward(side_length)
            ob.left(180 - angle_base)

            ob.penup()
            ob.goto(self.x, self.y)
            ob.write(self.label, align="center", font=("Arial", 16, "normal"))
            ob.pendown()

        draw_part()

    def _draw_to_svg(self, shape_group, drawer):
        base_length = self.width
        triangle_height = self.height

        # Calcular los puntos del triángulo
        points = [(self.x, self.y - triangle_height / 2),
                  (self.x + base_length / 2, self.y + triangle_height / 2),
                  (self.x - base_length / 2, self.y + triangle_height / 2)]
        
        # Añadir el triángulo al SVG con la posición ajustada
        shape_group.add(drawer.polygon(points))

        # Añadir la etiqueta en el centro
        shape_group.add(drawer.text(self.label, insert=(self.x, self.y), text_anchor="middle"))