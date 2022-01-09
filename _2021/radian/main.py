from manim import *
import math

class Radian(Scene):
    _fg = "#171717"
    _radius = 2
    _dot_radius = 0.065
    _width = 2
    font_size = 35
    font_family = "Minion Pro"
    med_buff=0.4
    colors = {
            "fg" : "#f1f1f1",
            "bg" : "#171717",
            "red" : "#cc1d24",
            "green" : GREEN_E,
            }
    def construct(self):
        self.camera.background_color = self.colors["bg"]
        text = ["1 \\text{ Rad}", "2 \\text{ Rad}", "3 \\text{ Rad}", "\pi \\text{ Rad}", "2\pi \\text{ Rad}"]
        _r = MathTex("r", color=self.colors['red'], font_size=50)
        plane = NumberPlane(
                x_range=[-10, 10, 1],
                y_range=[-10, 10, 1],
                background_line_style={
                    "stroke_color": GRAY_A,
                    "stroke_width": 0.5,
                    "stroke_opacity": 0.05
                    },
                axis_config = {
                    "stroke_width": 1,
                    "stroke_opacity": 0.1
                    }
                )


        circle = Circle(radius=2, stroke_color=self.colors["fg"], stroke_width=2)
        center = Dot(color=self.colors["red"]).move_to(circle.get_center())
        diameter = Line(start=circle.get_center(), end=circle.get_right(), stroke_color=self.colors["red"])
        diameter_copy = diameter.copy()
        diameter_copy.set_style(stroke_opacity=0)
        self.add(plane)
        self.play(GrowFromCenter(circle), FadeIn(center), GrowFromEdge(diameter, LEFT), run_time=2)
        self.play(Write(_r.next_to(diameter, DOWN)), run_time=3)
        self.wait()

        tangent_line = TangentLine(circle, alpha=0, length=diameter.get_length(), color=self.colors["red"]).shift(UP*1)
        self.play(Rotate(diameter, -PI/2, about_point=circle.get_right()), FadeOut(_r), run_time=3)
        self.wait(0.5)
        self.remove(diameter)
        self.add(tangent_line)

        arc = Arc(radius=self._radius, angle=1, stroke_color=self.colors["red"])
        line1 = Line(start=center.get_center(), end=arc.get_end(), color=self.colors["red"])
        trace = TracedPath(line1.get_end, stroke_color=self.colors["red"], stroke_width=4)
        # arc2 = always_redraw(lambda: ArcBetweenPoints(start=circle.get_right(), end=line1.get_end(), angle=1,  color=BLUE))

        # angle = always_redraw(lambda: Angle(line1, line2, color=self.colors["red"]))
        self.play(Transform(tangent_line, arc), run_time=1.5)
        self.play(Create(line1), run_time=1.5)
        angle = Angle(diameter_copy, line1, color=GRAY_C, stroke_width=2)
        txt_old = MathTex(text[0], font_size=self.font_size).next_to(center, DOWN, buff=self.med_buff)
        self.play(Create(angle), FadeIn(txt_old, shift=UP), run_time=3)
        #        2, 3, PI,   2PI
        steps = [1, 1, PI-3, PI]
        txt_new = txt_old
        self.add(trace)
        for step in range(len(steps)):
            line2 = line1.copy().set_style(stroke_color=GRAY_C, stroke_width=1)
            (a, b) = (
                    line1.copy().set_style(stroke_opacity=0),
                    line1.copy().set_style(stroke_opacity=0))
            self.play(Rotate(b, steps[step], about_point=center.get_center()))
            angle = Angle(a, b, color=GRAY_C, stroke_width=2)

            txt_old = txt_new
            txt_new = MathTex(text[step+1], font_size=self.font_size).next_to(center, DOWN, buff=self.med_buff)
            self.play(Rotate(line1, steps[step], about_point=center.get_center()),
                    FadeIn(line2.copy(), run_time=0.2),
                    FadeIn(Dot(radius=0.05, color=GRAY_C).move_to(line1.get_end()), run_time=0.2),
                    FadeOut(txt_old, shift=UP),
                    FadeIn(txt_new, shift=UP),
                    Create(angle),
                    rate_func=smooth,
                    run_time=3
                    )
        self.play(FadeIn(line2.copy(), run_time=0.2))
        self.play(FadeIn(Dot(radius=0.05, color=GRAY_C).move_to(line1.get_end()), run_time=0.2))
        self.wait(2)
        units = ["\\frac{\pi}{2}", "\pi", "\\frac{3}{2} \pi", "2 \pi"]
        places = [UP, LEFT, DOWN, RIGHT]
        unit_group = VGroup()
        for i in range(len(units)):
            unit_group.add(MathTex(units[i], font_size=self.font_size).next_to(circle, places[i]))
        self.play(AnimationGroup(FadeIn(unit_group), lag_ratio=0.3), FadeOut(txt_new), run_time=3)
        self.wait(3)

