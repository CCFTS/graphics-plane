from .ShapeModule import Shape
import math
class GraphicsPlane:
    def create_rectangle(width, height):
        shape = Shape("Rectangle")
        x, y = 0, 0

        shape.add_trace((x, y), (x + width, y))
        shape.add_trace((x + width, y), (x + width, y - height))
        shape.add_trace((x + width, y - height), (x, y - height))
        shape.add_trace((x, y - height), (x, y))

        return shape

    def create_triangle( base, height):
        shape = Shape("Triangle")
        x, y = 0, 0

        side = math.sqrt((base / 2) ** 2 + height ** 2)
        x2, y2 = base / 2, -height
        x3, y3 = -base / 2, -height

        shape.add_trace((x, y), (x2, y2))
        shape.add_trace((x2, y2), (x3, y3))
        shape.add_trace((x3, y3), (x, y))

        return shape


