import svgwrite
from .ShapeModule import Rectangle, Triangle

class GraphicsPlane:
    def create_rectangle(self, width, height, x=0, y=0):
        shape = Rectangle(width, height, label="Rectangle", x=x, y=y)
        return shape

    def create_triangle(self, base, height, x=0, y=0):
        shape = Triangle(base, height, label="Triangle", x=x, y=y)
        return shape

    def export_to_svg(self, shape, file_name):
        dwg = svgwrite.Drawing(file_name, profile='tiny')
        shape_group = dwg.add(dwg.g(id='shape', fill='none', stroke='black'))
        shape._draw_to_svg(shape_group, dwg)
        dwg.save()
        print(f"Figura exportada a {file_name}")
