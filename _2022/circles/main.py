from manim import *
import math
# config.frame_height = 16
# config.frame_width = 9
# config.pixel_height = 720
# config.pixel_width = 1366
config.background_color = "#045b7d"
class Circles(Scene):
    n = 250
    _dot_radius = 0.015
    _circle_radius = 3
    _BLUE = "#045b7d"
    _GREEN = "#455D3E"
    _YELLOW = "#fdaa26"
    _REDISH = "#f1ca91"
    _WHITE = "#ecebe9"
    _BLACK = "#3a3a3a"
    def construct(self):
        def draw_shape(k, n, radius):
            c = Circle(radius=radius, stroke_color=self._WHITE).to_edge(RIGHT)
            pos = [i*(360/n)*DEGREES for i in range(n)]
            lines = VGroup(*[Line(c.point_at_angle(i), c.point_at_angle(k*i%n), stroke_color=self._WHITE, stroke_width=1) 
                for i in pos])
            shape = VGroup(c, lines)
            return shape

        shapes = VGroup()
        for i in range(2, 102):
            shape = draw_shape(i, 250, self._circle_radius)
            shapes.add(shape)

        bg_shapes = VGroup(*[shape.copy().set_style(stroke_opacity=0.2) for shape in shapes])
        bg_shapes.arrange_in_grid(
                cols=10, rows=10, buff=1).scale_to_fit_width(
                        config.frame_width - (config.frame_width/2)).scale_to_fit_width(config.frame_height - 4)
        self.add(bg_shapes.to_edge(LEFT))
        for i in range(1, len(shapes)):
            self.play(Uncreate(shapes[i-1]), Create(shapes[i]), 
                    bg_shapes[i-1].animate.set_style(stroke_opacity=0.2),
                    bg_shapes[i].animate.set_style(stroke_opacity=1),
                    run_time=0.2)
        self.wait(2)
