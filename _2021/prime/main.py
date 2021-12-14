from manim import *


class NumberCircle(VGroup):
    def __init__(self, number, color=WHITE):
        VGroup.__init__(self)
        dot = LabeledDot(Text(str(number), color=color, font_size=19,
                              font="Ubuntu Mono"), radius=0.25, color="#1d2021")
        self.add(dot)


class ArrowDot(VGroup):
    def __init__(self, first, last):
        VGroup.__init__(self)
        arrow = Arrow(start=first.get_corner(UR), end=last.get_corner(DL), buff=0)
        self.add(arrow)


class WriteIfOdd(VGroup):
    def __init__(self, circle, text):
        VGroup.__init__(self)

        circle_red = NumberCircle(circle, self._red).scale(2).move_to(
            circle, ORIGIN).set_stroke(color=self._red, width=self.circle_width)
        self.add(text.next_to(circle_red, RIGHT))
        # self.play(Write(eq_odd), FadeOut(_7), FadeIn(_7_red))


class prime(Scene):
    _dim = "#1d2021"
    _bg = "#02042a"
    _red = "#cc241d"
    circle_width = 3

    def construct(self):
        # _code = Text("lambda x: x % 2 == 0", font="Sudo", font_size=30).to_edge(UP)
        self.camera.background_color = self._bg
        eq_odd = MathTex(r"\times {{3}} + 1", font_size=70)
        eq = MathTex(r" + 1", font_size=70)
        eq_even = MathTex(r"\div {{2}}", font_size=70)

        numbers = VGroup(*[NumberCircle(num) for num in range(1, 10)])
        self.play(numbers.animate.arrange(RIGHT, buff=0.3), run_time=2)
        self.wait()
        # copy numbers 7 and then delete it from numbers list
        _7 = numbers[6].copy()
        numbers.remove(numbers[6])
        #

        # self.play(_7.animate.shift(DOWN))
        # self.play(_7.animate.set_stroke(color=WHITE, width=self.circle_width))
        choosen_animations = [
            FadeIn(_7, stroke_color(WHITE, width=self.circle_width))
        ]
        self.play(AnimationGroup(*choosen_animations))
        # self.play(AnimationGroup(
        #     _7.shift(DOWN),
        #     _7.set_stroke(color=WHITE, width=self.circle_width)
        # ))
        self.wait()
        self.play(_7.animate.scale(2).move_to(ORIGIN),
                  FadeOut(numbers, shift=UP),
                  run_time=2)
        # _7_red = NumberCircle(7, self._red).scale(2).move_to(
        #     _7, ORIGIN).set_stroke(color=self._red, width=self.circle_width)
        # self.add(eq_odd.next_to(_7, RIGHT))
        # self.play(Write(eq_odd), FadeOut(_7), FadeIn(_7_red))
        # self.wait()
        # _21 = NumberCircle(21).scale(2)
        # arrow = always_redraw(lambda: Arrow(
        #     start=_7_red.get_corner(UR), end=_21.get_corner(DL), buff=0))
        # arrow = ArrowDot(_7_red, _21)
        # self.play(_7_red.animate.shift(LEFT*2, DOWN*3),
        #           Write(_21),
        #           Write(arrow),
        #           _21.animate.shift(UR),
        #           FadeOut(eq_odd),
        #           run_time=2)
        # _7.move_to(_7_red, ORIGIN)
        # self.play(FadeOut(_7_red), FadeIn(_7),
        #           run_time=0.5)
        # self.wait()
        # self.add(eq.next_to(_21, RIGHT))
        # self.play(Write(eq))
        # self.play(_21.animate.shift(UP))
        # self.wait()
