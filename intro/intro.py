#!/bin/env python
from manim import *


class Intro(Scene):
    def construct(self):
        c = Circle(color=WHITE)
        pi = MathTex('\pi', font_size=140)
        sub_text = Text("3Point14", font_size=35).shift(DOWN * 1.3)
        self.play(Create(c), run_time=2)
        self.wait(1.3)
        self.play(DrawBorderThenFill(pi), run_time=1.5)
        self.wait()
        self.play(Write(sub_text))
        self.wait(2)
