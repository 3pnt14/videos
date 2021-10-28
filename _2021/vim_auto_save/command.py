#!/bin/env python
from manim import *
class commands(Scene):
    cmd = "autocmd BufWritePost [FILE] ![ACTION] "
    cmd_exp = "autocmd BufWritePost /tmp/myfile !cp /tmp/myfile ~ "
    mono_font = "monaco"
    def construct(self):
        cmd = Text(self.cmd, font=self.mono_font, font_size=25, t2c={'autocmd': RED, '[7:19]': YELLOW})
        cmd_exp = Text(self.cmd_exp, font=self.mono_font, font_size=25, t2c={'autocmd': RED, '[7:19]': YELLOW})

        self.play(AddTextLetterByLetter(cmd), run_time=1)
        self.wait(0.2)
        self.play(cmd.animate.shift(UP*1.5), FadeIn(cmd_exp), run_time=1)
        self.wait(0.2)
        self.play(FadeOut(cmd), cmd_exp.animate.scale(0.5).to_corner(UL), buff=0.05)
        self.wait(1)
