from manim import *


class Quadratic(Scene):
    _bg = "#fff4d8"
    _fg = "#000000"
    _red = "#f97054"
    _blue = "#166f89"
    _green = "#1f9659"

    def construct(self):
        self.camera.background_color = self._bg

        def labeled_rectangle(W, H, x_label, y_label, color):
            res = VGroup()
            rec = Rectangle(width=W, height=H, stroke_color=color, stroke_width=2)
            x_label = MathTex(x_label, color=color).next_to(rec, UP).shift(DOWN * 0.7)
            y_label = MathTex(y_label, color=color).next_to(rec, LEFT).shift(RIGHT * 0.8)
            res.add(rec, x_label, y_label)
            return res

        # Text {{{1
        eq = [
            "{{x^2}} + {{26}}x &= {{27}}",             # Equation 0
            "{{x^2}} + {{26}}x &= {{27}} + {{169}}",  # Equation 1
            "{{x^2}} + {{26}}x &= {{196}}",  # Equation 2
            "{{x^2}} + {{26}}x &= {{(14)^2}}",  # Equation 3
            "{{x}} + {{13}} = 14",  # Equation 4
            "{{x}}  = 1",  # Equation 5
        ]

        eq1 = MathTex(r"{{x^2}} + {{26}}x &= {{27}}",
                      color=self._fg,
                      substrings_to_isolate=["26", "27"]).to_edge(UP)

        eq2 = MathTex(r"{{x^2}} + {{26}}x &= {{27}} + {{169}}", color=self._fg,
                      substrings_to_isolate=["26", "169"]).to_edge(UP)
        eq3 = MathTex(r"{{x^2}} + {{26}}x &= {{196}}", color=self._fg,
                      substrings_to_isolate=["26", "169", "196"]).to_edge(UP)
        eq4 = MathTex(r"{{x^2}} + {{26}}x &= {{(14)^2}}", color=self._fg,
                      substrings_to_isolate=["26", "169", "(14)^2"]).to_edge(UP)
        eq5 = MathTex(r"{{x}} + {{13}} = 14", color=self._fg,
                      substrings_to_isolate=["x", "13", "14"]).next_to(eq4, DOWN).align_to(eq4, ORIGIN)
        eq6 = MathTex(r"{{x}}  = 1", color=self._fg,
                      substrings_to_isolate="x").next_to(eq4, DOWN).align_to(eq5, ORIGIN)
        eq[1].set_color_by_tex("26", self._blue).to_edge(UP)
        eq2.set_color_by_tex("26", self._blue)
        eq2.set_color_by_tex("169", self._red)

        eq3.set_color_by_tex("x^2", self._green)
        eq3.set_color_by_tex("26", self._blue)
        eq3.set_color_by_tex("169", self._red)
        eq3.set_color_by_tex("196", self._fg)

        eq4.set_color_by_tex("x^2", self._green)
        eq4.set_color_by_tex("26", self._blue)

        eq5.set_color_by_tex("x", self._green)
        eq5.set_color_by_tex("13", self._blue)
        eq6.set_color_by_tex("x", self._green)
        # }}}
        # SQUARES {{{1
        sx2 = labeled_rectangle(2, 2, "x", "x", self._green)
        r26 = labeled_rectangle(9, 2, "26", "x", self._blue)
        r13_top = labeled_rectangle(4.5, 2, "13", "x", self._blue)
        r13_left = labeled_rectangle(2, 4.5, "x", "13", self._blue)
        s13_square = labeled_rectangle(4.5, 4.5, "13", "13", self._red)
        s13_area = MathTex("169", color=self._red, font_size=90).move_to(s13_square.get_center())
        s13 = VGroup(s13_square, s13_area)

        # }}}
        # Animation {{{1
        self.play(Write(eq[1]))
        self.play(Write(eq1))

        self.play(Write(sx2),
                  eq1.animate.set_color_by_tex("x^2", self._green), run_time=2)
        self.play(sx2.animate.shift(UP + LEFT * 1.2).scale(0.5))
        self.wait(0.5)
        self.play(Create(r26),
                  r26.animate.scale(0.5).next_to(sx2, RIGHT, buff=0).align_to(sx2, UP),
                  eq1.animate.set_color_by_tex("26", self._blue))
        self.wait()
        d_line = DashedLine(r26.get_bottom(),
                            r26.get_top()).set_stroke(color=self._blue, width=2)
        self.play(Create(d_line))

        r13_top.scale(0.5).next_to(sx2, RIGHT, buff=0).align_to(sx2, UP)
        r13_left.scale(0.5).next_to(sx2, DOWN, buff=0).align_to(sx2, LEFT)
        r13 = VGroup(r13_top, r13_left)

        self.play(ReplacementTransform(r26, r13),
                  Uncreate(d_line))
        self.wait(1)
        # ---------------------------------------------------
        self.play(Create(s13),
                  s13.animate.scale(0.5).next_to(r13_top, DOWN, buff=0).align_to(r13_top, LEFT),
                  TransformMatchingTex(eq1, eq2)
                  )
        # ---------------------------------------------------
        self.wait(2)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)
        s13_black = Square(side_length=4.5).set_stroke(color=self._fg)
        self.play(GrowFromCenter(s13_black),
                  s13_black.animate.scale(0.72).align_to(sx2, LEFT + UP),
                  )

        brace_left = BraceLabel(s13_black, "14", brace_direction=LEFT,
                                color=BLACK).set_color(self._fg)
        brace_down = BraceLabel(s13_black, "14", brace_direction=DOWN,
                                color=BLACK).set_color(self._fg)
        # brace_text = MathTex("14")
        # brace = BraceText(s13_black, "14").set_color(self._fg)
        self.play(TransformMatchingTex(eq3, eq4),
                  Write(brace_left),
                  Write(brace_down))
        self.wait(1)
        self.play(FadeOut(s13_black))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5),
                  FadeOut(r13_left),
                  FadeOut(brace_left),
                  FadeOut(s13_square),
                  FadeOut(s13_area),
                  brace_down.animate.next_to(sx2, DOWN).align_to(sx2, LEFT))
        self.wait(2)
        eq6.add_updater(lambda x: x.next_to(sx2, UP))
        self.play(FadeOut(eq5),
                  FadeOut(r13_top),
                  sx2.animate.scale(2).move_to(ORIGIN),
                  FadeIn(eq6),
                  eq6.animate.move_to(ORIGIN),
                  FadeOut(brace_down))
        self.wait(2)
        # }}}
