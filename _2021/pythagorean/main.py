from manim import *
import math


class Pythagorean(Scene):
    _width = 1
    def construct(self):
        VMobject.set_default(stroke_width=self._width)
        Text.set_default(font="Minion Pro")
        title = Text("Visual Proof of the Pythagorean theorem", font_size=30).to_edge(UP, buff=MED_SMALL_BUFF)
        title_line = Line(start=title.get_left(), end=title.get_right(), 
                stroke_opacity=[0, 1, 0], stroke_width=2
                ).next_to(title, DOWN, buff=MED_SMALL_BUFF)
        triangle = Polygon(
                [0, 2, 0], [0, 0 ,0], [-1, 0, 0],
                stroke_color=WHITE,
                fill_color=GRAY_BROWN, fill_opacity=0.8
                )
        a = MathTex("a").next_to(triangle, DOWN)
        b = MathTex("b").next_to(triangle, RIGHT)
        c = MathTex("c").next_to(triangle, LEFT).shift(RIGHT*0.5)
        a2_square = Square(side_length=1, fill_color=GREEN, fill_opacity=0.4).next_to(triangle, DOWN, buff=0)
        b2_square = Square(side_length=2, fill_color=BLUE, fill_opacity=0.4).next_to(triangle, RIGHT, buff=0)
        c2_square = Square(side_length=math.sqrt(5), 
                fill_color=RED, 
                fill_opacity=0.4).next_to(triangle, LEFT, buff=0).align_to(triangle, DOWN).rotate(-PI/6.74, about_point=[-1, 0, 0])
        self.add(triangle, a, b, c)
        self.play(Write(title), Write(title_line))

        a2 = MathTex("a^2", substrings_to_isolate="a^2").move_to(a2_square.get_center())
        b2 = MathTex("b^2", substrings_to_isolate="b^2").move_to(b2_square.get_center())
        c2 = MathTex("c^2", substrings_to_isolate="c^2").move_to(c2_square.get_center())
        self.play(Create(b2_square), Create(a2_square), Create(c2_square),
                ReplacementTransform(a, a2),
                ReplacementTransform(b, b2),
                ReplacementTransform(c, c2),
                # a2.animate.set_color_by_tex("a^2", GREEN_E),
                # b2.animate.set_color_by_tex("b^2", BLUE_E),
                # c2.animate.set_color_by_tex("c^2", RED_E))
                )

        a2.add_updater(lambda x: x.move_to(a2_square.get_center()))
        b2.add_updater(lambda x: x.move_to(b2_square.get_center()))
        c2.add_updater(lambda x: x.move_to(c2_square.get_center()))
        c2_triangle = triangle.copy()
        c2_group = VGroup(c2_square, c2_triangle)
        ab_group = VGroup(a2_square, b2_square, triangle)
        self.play(c2_group.animate.shift(LEFT*2).align_to(ab_group, DOWN), ab_group.animate.shift(RIGHT*2))

        ab_tri_down_up = triangle.copy().rotate(PI/2).next_to(b2_square, DOWN, buff=0)
        ab_tri_down_down = triangle.copy().rotate(-PI/2).next_to(a2_square, RIGHT, buff=0)
        ab_tri_left_left = triangle.copy().rotate(PI).next_to(a2_square, UP, buff=0)

        c2_tri_up = triangle.copy().rotate(PI/2).next_to(c2_square, UP, buff=0).align_to(c2_square, UR)
        c2_tri_down = triangle.copy().rotate(-PI/2).next_to(c2_square, DOWN, buff=0).align_to(c2_square, DL)
        c2_tri_left = triangle.copy().rotate(PI).next_to(c2_square, LEFT, buff=0).align_to(c2_square, UL)

        text = [
                "Both BIG squares are equal size",
                "With the same amount of empty space",
                ]
        txt1 = Text(text[0], font_size=25, font="Arial").to_edge(DOWN, buff=1)
        txt2 = Text(text[1], font_size=25, font="Arial").to_edge(DOWN, buff=1)


        self.play(Create(ab_tri_down_up), 
                ReplacementTransform(triangle.copy(), ab_tri_down_down), 
                ReplacementTransform(triangle.copy(), ab_tri_left_left), 
                ReplacementTransform(c2_triangle.copy(), c2_tri_up), 
                ReplacementTransform(c2_triangle.copy(), c2_tri_down), 
                ReplacementTransform(c2_triangle.copy(), c2_tri_left))

        c2_big_square = Square(side_length=3, stroke_width=3).move_to(c2_square.get_center())
        ab_big_square = Square(side_length=3, stroke_width=3).align_to(b2_square, UR)
        equal = MathTex("=", font_size=70).next_to(c2_big_square, RIGHT).shift(RIGHT*1.1)
        self.play(Create(c2_big_square), Write(txt1, run_time=1))
        self.play(Write(equal),)
        self.play(AnimationGroup(
                    FadeOut(
                        ab_tri_down_up, ab_tri_down_down,
                        ab_tri_left_left, c2_tri_up,
                        c2_tri_down, c2_tri_left,
                        triangle, c2_triangle,
                        # ab_1, ab_2, ab_3, ab_4,
                        # c2_1, c2_2, c2_3, c2_4
                        )
                    ), run_time=2)
        result = MathTex("{{c^2}} = {{a^2}} + {{b^2}}", 
                substrings_to_isolate=["c^2", "a^2", "b^2"],
                font_size=70).to_edge(DOWN, buff=1)

        result.set_color_by_tex("c^2", RED_E)
        result.set_color_by_tex("a^2", GREEN_E)
        result.set_color_by_tex("b^2", BLUE_E)
        old_eq = VGroup(a2, b2, c2)
        self.play(c2_big_square.copy().animate.move_to(ab_group.get_center()),  ReplacementTransform(txt1, txt2))
        self.wait()
        self.play(TransformMatchingShapes(old_eq, result), FadeOut(equal), FadeOut(txt2))
        self.wait(2)
