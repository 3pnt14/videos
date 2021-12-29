from manim import *
import math
class Radian(Scene):
    _fg = "#1d2021"
    _radius = 2
    _dot_radius = 0.065
    _width = 2
    def construct(self):
        text = [
                "r",
                "1 radian",
                "2 radian",
                "3 radian",
                "\\pi",
                "2\\pi",
                ]

        self.camera.background_color = WHITE
        circle = Circle(radius=self._radius, stroke_color=BLUE_E, stroke_width=self._width)
        center = Dot(color=BLACK, radius=self._dot_radius)
        line = Line(start=circle.get_center(), end=circle.get_right(), stroke_color=RED, stroke_width=self._width)
        (dot_end, dot_start) = Dot(color=RED, radius=self._dot_radius), Dot(color=RED, radius=self._dot_radius)
        dot_end.add_updater(lambda x: x.move_to(line.get_end()))
        dot_start.add_updater(lambda x: x.move_to(line.get_start()))
        self.play(FadeIn(circle), FadeIn(center))
        self.add(dot_end, dot_start)

        self.play(Create(line), run_time=0.3)
        self.wait(0.5)
        self.play(Rotate(line, -PI/2, about_point=[self._radius, 0, 0], run_time=0.3))
        self.wait()
