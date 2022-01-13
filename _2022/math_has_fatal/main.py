from manim import *


class Lines(Scene):
    _blue = "#020420"
    _fg   = "#e1e1e1"
    long_runtime = 5
    def long_wait(self):
        self.wait(5)
    def med_wait(self):
        self.wait(3)
    def short_wait(self):
        self.wait(1)
    numbs_font_size = 30
    Camera.background_color = _blue
    def construct(self):
        spec_numbers = [r"\frac{1}{3}", r"\sqrt{2}", r"\frac{5}{2}", r"e", r"\pi"]
        # adding math tex package
        temp = TexTemplate()
        # first change the font -> fourier
        # use mathrsfs package
        temp.add_to_preamble(r"\usepackage{mathrsfs}\usepackage{fourier}")
        natural = MathTex(r"\mathbb{N} \emph{atural}", tex_template=temp, font_size=40)
        real = MathTex(r"\mathbb{R} \emph{eal}", tex_template=temp, font_size=40)

        number_line = NumberLine(x_range=[-8, 8, 1], 
                include_numbers=True, 
                font_size=self.numbs_font_size,
                label_direction=UP*1.6,
                unit_size=1)
        # Creaing the orange (thick) line
        orange_line = NumberLine(x_range=[0, 10, 1], 
                include_numbers=True, 
                include_ticks=False, 
                tick_size=0.3,
                color=ORANGE,
                font_size=self.numbs_font_size,
                label_direction=UP*0.8,
                unit_size=1,
                stroke_width=10)
        # gb_line
        GB_line = Line(start=ORIGIN, end=RIGHT, stroke_color=[GREEN_E, BLUE_D], stroke_width=10).shift(DOWN*0.2)
        # setting numbers color to ORANGE
        [number.set_color(ORANGE) for number in orange_line.numbers[:]]
        # put it on to of the number line
        orange_line.shift(RIGHT*orange_line.get_length()/2 + UP*0.2)

        orange_line = Line(start=ORIGIN, end=RIGHT*9, stroke_color=ORANGE, stroke_width=10).shift(UP*0.2)
        self.play(Create(number_line), run_time=3)
        self.play(FadeIn(orange_line), runt_time=3)
        self.wait(1)
        natural.move_to(ORIGIN).shift(LEFT*2+UP*2)
        self.play(FadeIn(natural))
        self.play(orange_line.animate.next_to(natural, RIGHT).align_to(natural, DOWN))
        self.wait()
        self.play(FadeIn(GB_line))
        self.play(GB_line.animate.shift(DOWN*2, RIGHT))
        self.play(GB_line.animate.set_length(6))
        self.play(GB_line.animate.set_style(stroke_width=50))
        mini_number_line = NumberLine(
                x_range=[0, 1, 0.25],
                length=6,
                include_numbers=True,
                numbers_to_include=[0, 1],
                tick_size=0.2
                ).shift(DOWN*2, RIGHT)
        mini_number_line.align_to(GB_line, LEFT)
        self.play(Create(mini_number_line))

        self.med_wait()
