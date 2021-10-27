#!/bin/env python
from manim import *
# command {{{ 1 
class commands (Scene):
    cmd = "autocmd BufWritePost <Path to the file> !<Commands>" 
    cmd_exp = "autocmd BufWritePost /tmp/myfile !cp /tmp/myfile ~"
    autocmd = "autocmd"
    mono_font = "monaco"
    run_time=1.5
    def construct(self):
        cmd = Text(self.cmd, font_size=15, font=self.mono_font, t2c={"autocmd": RED, '[7:19]': YELLOW})
        cmd_exp = Text(self.cmd_exp, font_size=15, font=self.mono_font, t2c={"autocmd": RED, '[7:19]': YELLOW})
        self.play(AddTextLetterByLetter(cmd), run_time=1.5)
        self.wait(0.5)
        autocmd = Text(self.autocmd, font_size=30, font=self.mono_font, color=RED)
        self.play(cmd.animate.shift(UP))
        self.play(cmd.animate.shift(UP), FadeIn(cmd_exp))
        self.wait(2)
# }}}

