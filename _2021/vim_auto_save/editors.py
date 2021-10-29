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
        episodes = VGroup(*[yt_logo.shift(i * 1.03 * RIGHT) for i in range(1, 12)])
        self.play(Write(episodes))
        self.wait(2)
        # self.play(DrawBorderThenFill(yt_logo))
        # self.wait()
        # self.play(yt_logo.animate.scale(0.3).to_corner(UL), buff=3)
        # self.wait()
        # ext_yt_logo = yt_logo.copy()
        # for i in range(12):
            # i = ext_yt_logo.copy().animate.shift(RIGHT * 1.03)
            # self.play(i, run_time=0.3)
            # ext_yt_logo.shift(RIGHT * 1.03)
        # self.wait(2)
