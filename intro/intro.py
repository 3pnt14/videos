#!/bin/env python
from manim import *


class Intro(Scene):

    def construct(self):
        circle = Circle(radius=2).set_color(WHITE)
        pi = MathTex(r'\pi', font_size=140).scale(2)
        sub_text = Text("3Point14", font_size=90)

        # Scenes
        self.play(Create(circle), run_time=1)
        self.wait()
        self.play(DrawBorderThenFill(pi))
        self.wait(2)
