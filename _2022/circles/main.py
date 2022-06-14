from manim import *
import math

config.background_color = "#455D3E"
class Circles(Scene):
    n = 250
    _dot_radius = 0.015
    _BLUE = "#045b7d"
    _GREEN = "#455D3E"
    _YELLOW = "#fdaa26"
    _REDISH = "#f1ca91"
    _WHITE = "#ecebe9"
    _BLACK = "#3a3a3a"
    def construct(self):
        def draw_shape(k, n, radius):
            c = Circle(radius=radius, stroke_color=self._WHITE)
            pos = [i*(360/n)*DEGREES for i in range(n)]
            lines = VGroup(*[Line(c.point_at_angle(i), c.point_at_angle(k*i%n), stroke_color=self._WHITE, stroke_width=1) 
                for i in pos])
            shape = VGroup(c, lines)
            return shape

        shapes = VGroup()
        for i in range(2, 251):
            shape = draw_shape(i, 250, 2.5)
            # self.play(Create(shape[0]))
            # self.wait()
            # self.play(Create(shape[1], lag_ratio=0.2), run_time=4)
            # self.wait()
            shapes.add(shape)
            # self.play(FadeOut(shape))
        # self.play(Create(shapes[0]), run_time=0.25)
        for i in range(1, len(shapes)):
            self.play(Uncreate(shapes[i-1]), Create(shapes[i]), run_time=0.2)
        self.wait(2)
