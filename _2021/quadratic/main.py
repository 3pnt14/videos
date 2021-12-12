from manim import *


class LabeledRectangle(VGroup):
    """A regual Rectangle with label on top and on side"""

    def __init__(self, W, H, x_label, y_label):
        VGroup.__init__(self)
        rec = Rectangle(width=W, height=H, stroke_width=2)
        x_label = MathTex(x_label).next_to(rec, UP).shift(DOWN * 0.6)
        y_label = MathTex(y_label).next_to(rec, LEFT).shift(RIGHT * 0.7)
        res = VGroup(rec, x_label, y_label)
        self.add(res)


class Defaults(Scene):
    _bg = "#fff4d8"
    _fg = "#000000"
    _red = "#f97054"
    _blue = "#166f89"
    _green = "#1f9659"
    MathTex.set_default(color=_fg)


class Quadratic(Defaults):

    def construct(self):
        self.camera.background_color = self._bg
        # Text
        eqs = [
            "{{x^2}} + {{26}}x &= {{27}}",
            "{{x^2}} + {{26}}x &= {{27}} + {{169}}",
            "{{x^2}} + {{26}}x &= {{196}}",
            "{{x^2}} + {{26}}x &= {{(14)^2}}",
            "{{x}} + {{13}}x &= {{14}}",
            "{{x}} &= {{1}}",
        ]
        eq1, eq2, eq3, eq4, eq5, eq6 = MathTex(eqs[0]), MathTex(eqs[1]), MathTex(
            eqs[2]), MathTex(eqs[3]), MathTex(eqs[4]), MathTex(eqs[5])

        for i in [eq1, eq2, eq3, eq4, eq5, eq6]:
            i.to_edge(UP)
        # Shapes
        x2 = LabeledRectangle(2, 2, "x", "x").set_color(self._green)
        r26 = LabeledRectangle(4.5, 1, "26", "x").set_color(self._blue)
        # Animations
        self.play(Write(eq1))
        self.play(Write(x2),
                  eq1.animate.set_color_by_tex("x^2", self._green))
        self.play(x2.animate.scale(0.5).shift(UL))
        self.play(Write(r26),
                  r26.animate.next_to(x2, RIGHT, buff=0),
                  eq1.animate.set_color_by_tex("26", self._blue))
        self.wait(1)
        self.play(Write(DashedLine(r26.get_bottom(), r26.get_top()).set_stroke(color=self._blue)))
        self.wait(1)
