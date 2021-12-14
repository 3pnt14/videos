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
        self.play(GrowArrow(arrow))


class WriteIfOdd(VGroup):
    def __init__(self, circle, text):
        VGroup.__init__(self)

        circle_red = NumberCircle(circle, self._red).scale(2).move_to(
            circle, ORIGIN).set_stroke(color=self._red, width=self.circle_width)
        self.add(text.next_to(circle_red, RIGHT))
        # self.play(Write(eq_odd), FadeOut(_7), FadeIn(_7_red))


class Collatz(Scene):
    _dim = "#1d2021"
    _bg = "#02042a"
    _red = "#cc241d"
    circle_width = 3

    def construct(self):
        # _code = Text("lambda x: x % 2 == 0", font="Sudo", font_size=30).to_edge(UP)
        self.camera.background_color = self._bg

        def change_color(self, circle, color):
            circle_copy = NumberCircle(circle, color).scale(2).move_to(
                circle, ORIGIN).set_stroke(color=color, width=self.circle_width)
            self.play(FadeIn(circle_copy, circle))

        eq_odd = MathTex(r"\times 3 + 1", font_size=70)
        eq = MathTex(r" + 1", font_size=70)
        eq_even = Text(r"÷ 2", font_size=50)

        numbers = VGroup(*[NumberCircle(num) for num in range(1, 10)]).shift(LEFT*3)
        self.play(numbers.animate.arrange(RIGHT, center=False,
                                          buff=0.3), rate_func=smooth, run_time=2)
        self.wait()
        # copy numbers 7 and then delete it from numbers list
        # _7 = numbers[6].copy()
        # numbers.remove(numbers[6])

        def choose_number(number):
            _number = numbers[number-1].copy()
            numbers.remove(numbers[number-1])
            self.play(AnimationGroup(
                _number.animate.set_stroke(color=WHITE, width=self.circle_width),
                FadeOut(numbers, shift=UP),
                rate_func=rush_from,
                run_time=2
            ))
            return _number
        _7 = choose_number(7)
        #
        self.wait()
        self.play(_7.animate.scale(2).move_to(ORIGIN), run_time=2)

        def is_even(number):
            return number % 2 == 0

        def change_color(number, old, change=False):
            if is_even(number):
                new = NumberCircle(number, BLUE).scale(
                    2).set_stroke(color=BLUE, width=self.circle_width).move_to(old, ORIGIN)
                eq_even.next_to(new, RIGHT)
                self.play(FadeIn(new), FadeOut(old), Write(eq_even))
                return new, int((number / 2))
            else:
                new = NumberCircle(number, RED).scale(2).set_stroke(
                    color=RED, width=self.circle_width).move_to(old, ORIGIN)
                eq_odd.next_to(new, RIGHT)
                self.play(FadeIn(new), FadeOut(old), Write(eq_odd))
                return new, int((number * 3 + 1))

        def write_arrow_up(start, end):
            arrow = Arrow(start=start.get_corner(UR),
                          end=end.get_corner(DL),
                          buff=3.1,
                          stroke_width=5)
            return arrow

        def write_arrow_down(start, end):
            arrow = Arrow(start=start.get_corner(DR), end=end.get_corner(UL), buff=3.1)
            return arrow

        new, res = change_color(7, _7)
        self.wait()
        test = NumberCircle(res).scale(2).shift(UP*3+RIGHT*2)
        arrow = write_arrow_up(new, test)
        self.play(Write(test), GrowArrow(arrow))

        change_color(res, test)
        self.wait(3)
