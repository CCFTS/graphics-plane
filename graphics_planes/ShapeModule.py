import svgwrite

class Shape:
    def __init__(self, name):
        self.name = name
        self.traces = []

    def add_trace(self, start, end):
        """Adds a trace to the shape."""
        self.traces.append((start, end))

    def export_to_svg(self, filename):
        """Exports the shape to an SVG file."""
        dwg = svgwrite.Drawing(filename, profile='tiny')
        for trace in self.traces:
            start, end = trace
            dwg.add(dwg.line(start=start, end=end, stroke=svgwrite.rgb(0, 0, 0, '%')))
        dwg.save()
        print(f"Shape exported to {filename}")

    def show_traces(self):
        """Shows all traces of the shape (for debugging purposes)."""
        for trace in self.traces:
            print(f"Start: {trace[0]}, End: {trace[1]}")
