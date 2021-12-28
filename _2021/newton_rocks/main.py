from manim import *

import manimpango
class NewtonRocks(Scene):
    def construct(self):
        # self.camera.background_image = "./newton.jpg"
        back = ImageMobject("./newton.jpg")
        glasses = ImageMobject("./glasses.png").scale(0.5).shift(UP*2.12+RIGHT*0.35)
        newtons_eyes = Dot().shift(UP)
        rec = SurroundingRectangle(back, buff=0, stroke_color=WHITE)
        self.add(back, rec)
        Text.set_default(font_size=40, font="Keep Calm", weight=BOLD)
        text = [
                "KEEP",
                "CALM",
                "AND",
                "LOVE",
                "NEWTON",
                ]
        txt0 = Text(text[0])
        txt1 = Text(text[1])
        txt2 = Text(text[2], font_size=20, weight=BOOK)
        txt3 = Text(text[3])
        txt4 = Text(text[4])
        txt_grid = VGroup(txt0, txt1, txt2, txt3, txt4).arrange_in_grid(rows=5, col_alignments="c").to_edge(DOWN, buff=1)
        self.play(FadeIn(txt_grid, shift=UP*0.5))
        self.play(FadeIn(glasses, shift=(UP+LEFT)), run_time=1.2)
        self.wait(1)

