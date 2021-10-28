#!/bin/python
from manim import *
class test(Scene):
    # Scenes
    def construct(self):
        yt_logo = SVGMobject(f"./youtube-logo.svg")
        self.play(DrawBorderThenFill(yt_logo))
        self.wait()
        self.play(yt_logo.animate.scale(0.3).to_corner(UL), buff=3)
        self.wait()
        temp_yt_logo = yt_logo.copy()
        lst = []
        for i in range(12):
            i = temp_yt_logo.copy().animate.shift(RIGHT * 1.03)
            lst.append(i)
            temp_yt_logo.shift(RIGHT * 1.03)
        for i in lst:
            self.get_attrs(i)
            self.play(i, run_time=0.3)
        self.wait(2)
