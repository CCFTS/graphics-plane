
import svgwrite

class Plane:
    def __init__(self, name="Drawing"):
        self.name = name
        self.shapes = []

    def add_shape(self, shape):
        """Adds a shape to the drawing."""
        self.shapes.append(shape)

    def export_to_svg(self, filename):
        """Exports the entire drawing to an SVG file."""
        dwg = svgwrite.Drawing(filename, profile='tiny')
        for shape in self.shapes:
            for trace in shape.traces:
                start, end = trace
                dwg.add(dwg.line(start=start, end=end, stroke=svgwrite.rgb(0, 0, 0, '%')))
        dwg.save()
        print(f"Drawing exported to {filename}")

    def show_shapes(self):
        """Shows all shapes and their traces in the drawing (for debugging purposes)."""
        for shape in self.shapes:
            print(f"Shape: {shape.name}")
            shape.show_traces()
