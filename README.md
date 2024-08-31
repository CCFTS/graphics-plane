
# graphics-plane

`graphics-plane` es una librería de Python para crear gráficos en 2D y exportarlos a formato SVG. Permite generar y manipular figuras geométricas como rectángulos y triángulos, y combinar varias figuras en un único dibujo.

## Instalación

Puedes instalar `graphics-plane` desde PyPI usando pip. Ejecuta el siguiente comando en tu terminal:

```bash
pip install graphics-plane
```

## Uso Básico

### Importar la Librería

Primero, importa las clases necesarias en tu script:

```python
from graphics_plane import DrawingTool, Drawing
```

### Crear Figuras y Dibujo

1. **Crear una instancia de `DrawingTool`** para generar figuras:

   ```python
   drawing_tool = DrawingTool()
   ```

2. **Crear un objeto `Drawing`** para manejar el conjunto de figuras:

   ```python
   drawing = Drawing("Sample Drawing")
   ```

3. **Generar figuras y añadirlas al dibujo**:

   ```python
   # Crear un rectángulo y un triángulo
   rectangle = drawing_tool.create_rectangle(100, 50)
   triangle = drawing_tool.create_triangle(100, 80)

   # Añadir las figuras al dibujo
   drawing.add_shape(rectangle)
   drawing.add_shape(triangle)
   ```

4. **Mostrar y exportar el dibujo**:

   ```python
   # Mostrar las figuras en el dibujo (para depuración)
   drawing.show_shapes()

   # Exportar el dibujo completo a SVG
   drawing.export_to_svg("sample_drawing.svg")
   ```

## Clases y Métodos

### `Shape`

Representa una forma geométrica. Puedes agregar trazos y exportar la figura a SVG.

- **Métodos**:
  - `add_trace(start, end)`: Agrega un trazo a la figura.
  - `export_to_svg(filename)`: Exporta la figura a un archivo SVG.
  - `show_traces()`: Muestra los trazos de la figura (para depuración).

### `DrawingTool`

Proporciona métodos para crear formas geométricas básicas.

- **Métodos**:
  - `create_rectangle(width, height)`: Crea un rectángulo con el ancho y alto especificados.
  - `create_triangle(base, height)`: Crea un triángulo con la base y altura especificadas.

### `Drawing`

Maneja un conjunto de formas y permite exportar el dibujo completo a SVG.

- **Métodos**:
  - `add_shape(shape)`: Añade una forma al dibujo.
  - `export_to_svg(filename)`: Exporta el dibujo completo a un archivo SVG.
  - `show_shapes()`: Muestra todas las formas y sus trazos (para depuración).

## Ejemplos

Aquí tienes un ejemplo completo de cómo usar la librería para crear y exportar un dibujo:

```python
from graphics_plane import DrawingTool, Drawing

# Crear una instancia de DrawingTool
drawing_tool = DrawingTool()

# Crear un objeto Drawing
drawing = Drawing("Sample Drawing")

# Crear un rectángulo y un triángulo
rectangle = drawing_tool.create_rectangle(100, 50)
triangle = drawing_tool.create_triangle(100, 80)

# Añadir las figuras al dibujo
drawing.add_shape(rectangle)
drawing.add_shape(triangle)

# Mostrar las figuras en el dibujo
drawing.show_shapes()

# Exportar el dibujo completo a SVG
drawing.export_to_svg("sample_drawing.svg")
```

## Mantenedores

Este proyecto es mantenido por:

- **Damián Zsiros**  
  [GitHub](https://github.com/damiansziros)  
  ![GitHub](https://img.shields.io/badge/GitHub-damiansziros-lightgrey?logo=github&logoColor=white)

- **Alejandro Beltrán**  
  [GitHub](https://github.com/alejandrobeltran)  
  ![GitHub](https://img.shields.io/badge/GitHub-alejandrobeltran-lightgrey?logo=github&logoColor=white)

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o deseas mejorar la librería, abre un [issue](https://github.com/tu_usuario/graphics-plane/issues) o envía un pull request en el [repositorio](https://github.com/tu_usuario/graphics-plane).

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
