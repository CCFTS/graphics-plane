from graphics_planes import GraphicsPlane,Plane
drawing = Plane("Sample Drawing")
# Crear un rectÃ¡ngulo y un triÃ¡ngulo
rectangle = GraphicsPlane.create_rectangle(100, 50)
triangle = GraphicsPlane.create_triangle(100, 80)

# AÃ±adir las figuras al dibujo
drawing.add_shape(rectangle)
drawing.add_shape(triangle)

# Mostrar las figuras en el dibujo (para depuraciÃ³n)
drawing.show_shapes()

# Exportar el dibujo completo a SVG
drawing.export_to_svg("sample_drawing.svg")