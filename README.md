
# graphics-plane

`graphics-plane` es una librería de Python para crear gráficos en 2D y exportarlos a formato SVG. Permite generar y manipular figuras geométricas como rectángulos y triángulos, y combinarlas en un único dibujo dentro de un plano definido.

## Instalación

Puedes instalar `graphics-plane` desde PyPI usando pip. Ejecuta el siguiente comando en tu terminal:

```bash
pip install graphics-plane
```

## Uso Básico

### Importar la Librería

Primero, importa las clases necesarias en tu script:

```python
from graphics_plane import Plane, Rectangle, Triangle
```

### Crear Figuras y Dibujo

1. **Crear un objeto `Plane`** especificando el ancho y alto del área de trabajo:

   ```python
   plane = Plane(name="Sample Plane", width=200, height=200)
   ```

2. **Crear instancias de las figuras**:

   ```python
   # Crear un rectángulo y un triángulo con posiciones específicas
   rectangle = Rectangle(width=100, height=50, label="My Rectangle", x=50, y=50)
   triangle = Triangle(width=100, height=80, label="My Triangle", x=100, y=100)
   ```

3. **Añadir las figuras al plano**:

   ```python
   # Añadir las figuras al plano
   plane.add_shape(rectangle)
   plane.add_shape(triangle)
   ```

4. **Mostrar y exportar el plano**:

   ```python
   # Mostrar las figuras en el plano (para depuración)
   plane.show_shapes()

   # Exportar el plano completo a SVG
   plane.export_to_svg("sample_plane.svg")
   ```

## Clases y Métodos

### `Shape`

Representa una forma geométrica. Puedes definir la posición y exportar la figura a SVG.

- **Atributos**:
  - `width`: Ancho de la figura.
  - `height`: Alto de la figura.
  - `label`: Etiqueta de la figura.
  - `x`: Posición horizontal en el plano.
  - `y`: Posición vertical en el plano.

- **Métodos**:
  - `draw(drawer)`: Dibuja la figura usando un objeto `drawer` (para exportación a SVG o para depuración con `turtle`).
  - `export_to_svg(drawer, file_name)`: Exporta la figura a un archivo SVG.
  - `_draw_to_svg(shape_group, drawer)`: Método interno para añadir la figura al SVG.

### `Rectangle`

Representa un rectángulo y hereda de `Shape`.

- **Métodos**:
  - `draw(drawer)`: Dibuja el rectángulo utilizando `turtle`, centrado en la posición (`x`, `y`).
  - `_draw_to_svg(shape_group, drawer)`: Añade el rectángulo al SVG con la posición ajustada.

### `Triangle`

Representa un triángulo y hereda de `Shape`.

- **Métodos**:
  - `draw(drawer)`: Dibuja el triángulo utilizando `turtle`, centrado en la posición (`x`, `y`).
  - `_draw_to_svg(shape_group, drawer)`: Añade el triángulo al SVG con la posición ajustada.

### `Plane`

Maneja un conjunto de formas y permite exportar el dibujo completo a SVG.

- **Atributos**:
  - `width`: Ancho del plano.
  - `height`: Alto del plano.
  - `shapes`: Lista de figuras en el plano.

- **Métodos**:
  - `add_shape(shape)`: Añade una forma al plano.
  - `export_to_svg(filename)`: Exporta el plano completo a un archivo SVG.
  - `show_shapes()`: Muestra todas las formas y sus posiciones utilizando `turtle` (para depuración).
  - `show_with_turtle()`: Utiliza `turtle` para dibujar todas las figuras en el plano, brindando una representación visual interactiva.

## Ejemplos

Aquí tienes un ejemplo completo de cómo usar la librería para crear y exportar un dibujo:

```python
from graphics_plane import Plane, Rectangle, Triangle

# Crear una instancia de Plane
plane = Plane(name="Sample Plane", width=200, height=200)

# Crear un rectángulo y un triángulo
rectangle = Rectangle(width=100, height=50, label="My Rectangle", x=50, y=50)
triangle = Triangle(width=100, height=80, label="My Triangle", x=100, y=100)

# Añadir las figuras al plano
plane.add_shape(rectangle)
plane.add_shape(triangle)

# Mostrar las figuras en el plano
plane.show_shapes()

# Exportar el plano completo a SVG
plane.export_to_svg("sample_plane.svg")
```

## Mantenedores

Este proyecto es mantenido por:

- **Damián Zsiros**  
  [GitHub](https://github.com/Damian-Zsiros-Prog)  
  ![GitHub](https://img.shields.io/badge/GitHub-Damian--Zsiros--Prog-lightgrey?logo=github&logoColor=white)

- **Alejandro Beltrán**  
  [GitHub](https://github.com/Beltranposso)  
  ![GitHub](https://img.shields.io/badge/GitHub-Beltranposso-lightgrey?logo=github&logoColor=white)

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o deseas mejorar la librería, abre un [issue](https://github.com/tu_usuario/graphics-plane/issues) o envía un pull request en el [repositorio](https://github.com/tu_usuario/graphics-plane).

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).