from manim import *
import math

class Radian(Scene):
    _fg = "#171717"
    _radius = 2
    _dot_radius = 0.065
    _width = 2
    font_size = 35
    font_family = "Minion Pro"
    colors = {
            "fg" : "#171717",
            "bg" : "#e1e1e1",
            "red" : "#cc1d24",
            }
    def construct(self):
        self.camera.background_color = self.colors["bg"]
        text = ["1 Rad", "2 Rad", "3 Rad", "\pi"]


        circle = Circle(radius=2, stroke_color=BLACK)
        center = Dot(color=self.colors["red"]).move_to(circle.get_center())
        diameter = Line(start=circle.get_center(), end=circle.get_right(), stroke_color=self.colors["red"])
        self.add(circle, center, diameter)

        tangent_line = TangentLine(circle, alpha=0, length=diameter.get_length(), color=self.colors["red"]).shift(UP*1)
        self.play(Rotate(diameter, -PI/2, about_point=circle.get_right()))
        self.wait(0.5)
        self.remove(diameter)
        self.add(tangent_line)

        arc = Arc(radius=self._radius, angle=1, stroke_color=self.colors["red"])
        arc2 = Arc(radius=self._radius, angle=1, start_angle=1, stroke_color=self.colors["red"])
        arc3 = Arc(radius=self._radius, angle=1, start_angle=2, stroke_color=self.colors["red"])
        self.play(Transform(tangent_line, arc), run_time=0.5)
        line1 = Line(start=circle.get_center(), end=arc.get_start(), color=GREEN)
        line2 = Line(start=circle.get_center(), end=arc.get_end(), color=BLUE)
        line1.add_updater(lambda x: x.put_start_and_end_on(circle.get_center(), arc.get_start()))
        line2.add_updater(lambda x: x.put_start_and_end_on(circle.get_center(), arc.get_end()))
        angle = Angle(line1, line2, color=GREEN).set_color(GREEN)
        _shape = VGroup(arc, angle)
        trace = TracedPath(line2.get_end, stroke_color=self.colors["red"], stroke_width=4)
        self.wait()
        txt1 = Text(text[0], color=GREEN, font_size=self.font_size, font=self.font_family).next_to(center, DOWN)
        self.play(Create(line1), Create(line2), Create(angle), Write(txt1))
        self.add(trace)
        self.wait()
        for _angle in [1, PI-2, PI]:
            self.play(Rotate(_shape, _angle, about_point=circle.get_center()), run_time=2)
        self.wait()

