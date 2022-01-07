from manim import *
import math

class Radian(Scene):
    _fg = "#171717"
    _red = "#cc1d24"
    _radius = 2
    _dot_radius = 0.065
    _width = 2
    def construct(self):
        self.camera.background_color = "#e1e1e1"
        def draw_arc(length):
            arc = Arc(radius=self._radius, angle=length, stroke_color=self._red)
            self.play(Write(arc))
            return arc

        circle = Circle(radius=2, stroke_color=BLACK)
        center = Dot(color=RED).move_to(circle.get_center())
        diameter = Line(start=circle.get_center(), end=circle.get_right(), stroke_color=RED)
        self.add(circle, center, diameter)

        tangent_line = TangentLine(circle, alpha=0, length=diameter.get_length(), color=RED).shift(UP*1)
        self.play(Rotate(diameter, -PI/2, about_point=circle.get_right()))
        self.remove(diameter)
        self.add(tangent_line)

        arc = Arc(radius=self._radius, angle=1, stroke_color=self._red)
        self.play(Transform(tangent_line, arc), run_time=0.5)
        self.wait()
