from manim import *
import math


class Defaults(Scene):

    # Scene Configuration
    # -------------------
    _bg = "#02042a"
    _sq_length = 3
    Text.set_default(color=WHITE)

    def small_pause(self, n=0.5):
        self.wait(n)

    def medium_pause(self, n=1):
        self.wait(n)

    def long_pause(self, n=2):
        self.wait(n)


class sq (Defaults):
    def construct(self):
        self.camera.background_color = self._bg
        title = Title("Quadratic proof")
        # Sounds
        # ------
        # Shapes
        # -------
        outer_square = Square(side_length=self._sq_length)
        outer_square_copy = outer_square.copy()
        inner_square = Square(side_length=(self._sq_length/math.sqrt(2)),
                              stroke_color=WHITE,
                              fill_color=ORANGE,
                              fill_opacity=1.0)

        inner_square.rotate(20*DEGREES)
        dot = Dot()
        # -----
        d_left_line = DashedLine(outer_square.get_bottom(),
                                 outer_square.get_top()).next_to(outer_square, LEFT).add_tip(tip_length=0.15)
        d_bottom_line = DashedLine(outer_square.get_left(),
                                   outer_square.get_right()).next_to(outer_square, DOWN).add_tip(tip_length=0.15)
        d_left_line.add_updater(lambda x: x.next_to(outer_square, LEFT))
        d_bottom_line.add_updater(lambda x: x.next_to(outer_square, DOWN))

        # Equations
        # ---------
        eq1 = MathTex("{{c^2}} = {{a^2}} + {{b^2}}")
        c2 = MathTex("{{c^2}}").add_updater(lambda x: x.move_to(inner_square.get_center()))
        a2 = MathTex("{{a^2}}")
        b2 = MathTex("{{b^2}}")
        eq1.add_updater(lambda x: x.next_to(outer_square, DOWN*4))

        self.play(Write(title))
        # Animation
        # ---------
        self.play(DrawBorderThenFill(outer_square))
        self.medium_pause()

        self.play(FadeOut(title))

        self.play(DrawBorderThenFill(inner_square))
        self.play(outer_square.animate.set_fill(YELLOW_E, opacity=.9))
        self.play(Write(eq1), Write(c2))
        self.play(Create(d_left_line), Create(d_bottom_line))

        self.long_pause()

        self.play(outer_square.animate.shift(LEFT*3), inner_square.animate.shift(LEFT*3))
        self.small_pause()

        self.play(FadeIn(outer_square_copy), outer_square_copy.animate.shift(RIGHT*3))
        self.small_pause()
