from manim import *
import math

class Radian(Scene):
    _fg = "#1d2021"
    _radius = 2
    _dot_radius = 0.065
    _width = 2
    def construct(self):
        self.camera.background_color = "#e1e1e1"
        c = Circle(radius=2, stroke_color=BLACK)
        center = Dot(color=RED).move_to(c.get_center())
        line = Line(start=c.get_center(), end=c.get_right(), stroke_color=RED)
        self.add(c, center, line)
        self.play(Rotate(line, -PI/2, about_point=c.get_right()))
        arc = Arc(radius=2, angle=1, stroke_color=RED)
        self.play(Swap(line, arc))
        self.wait()
