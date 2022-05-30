from manim import *
config.frame_rate = 60


# _Angle{{{1
class _Angle(Scene):
    def construct(self):
        line1 = Line(ORIGIN, RIGHT*3)
        line2 = Line(ORIGIN, LEFT*2+UP*np.sqrt(5))
        angle = Angle(line1, line2, radius=0.4)
        arc = ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=line1.get_length())
        dot = Dot(radius=0.1).move_to(line2.get_end()) 
        fill = VMobject()
        pnts = [line1.get_end(), line1.get_start(), line2.get_end()]
        fill.set_points_as_corners(pnts).add(arc.copy())
        fill.set_fill(BLUE, opacity=0.5)
        shape = VGroup(line1, line2, angle, arc, dot, fill)

        self.play(FadeIn(shape))
        fill.save_state()
        self.play(fill.animate.scale(0.9).set_style(stroke_color=YELLOW, fill_color=YELLOW), run_time=2)
        self.play(Restore(fill), run_time=2)
        self.wait()
# }}}
# RolledAngle {{{1
class RolledAngle(Scene):
    def construct(self):
        Dot.set_default(radius=0.08)
        Text.set_default(font_size=40)
        Polygon(stroke_width=1.5)

        dot_origin = Dot().move_to(ORIGIN)
        line1 = Line(ORIGIN, RIGHT*3)
        dot1 = Dot().move_to(line1.get_end())
        line2 = Line(ORIGIN, RIGHT*3 + UP*0.001)
        dot2 = Dot().move_to(line2.get_end())
        dot2.add_updater(lambda x: x.move_to(line2.get_end()))
        # angles
        angle = Angle(line1, line2, radius=0.5)
        arc = ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=line1.get_length())
        angle.add_updater(lambda x: x.become(Angle(line1, line2, radius=0.5)))
        arc.add_updater(lambda x: x.become(ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=line1.get_length())))

        deg = ValueTracker().next_to(angle, UP)
        deg.add_updater(lambda x: x.set_value(angle.get_value(degrees=True)))
        self.add(line1, line2, dot1, dot2, dot_origin, angle, deg, arc)

        c = Circle(radius=line1.get_length(), stroke_opacity=0)
        dots = VGroup(*[Dot(point=c.point_at_angle(i*DEGREES)) for i in [0, 20, 40, 60, 80, 100, 120, 140]])
        lines = VGroup(*[Line(dot_origin, dots[i].get_end(), stroke_opacity=0).scale(1.2)  for i in range(len(dots))])
        self.add(lines)
        # numbers.add(Text("0").next_to(dot_origin, DOWN*0.5))
        self.play(Rotate(line2, angle=140*DEGREES, about_point=ORIGIN), run_time=2)
        # self.play(FadeIn(dots), FadeIn(numbers))
        self.play(FadeIn(dots))

        ####################
        # CREATING TRIANGLES
        ####################
        points = [list(c.point_at_angle(i*DEGREES)) for i in [0, 20, 40, 60, 80, 100, 120, 140]] 
        print(points[i+1])
        # triangles = VGroup(*[RegularPolygon(points[1], points[i+1], points[i+2]) for i in len(points)])
        triangles = VGroup(*[Polygon(dot_origin.get_center(), points[i], points[i+1]) for i in range(len(points)-1)])
        triangles.set_style(fill_opacity=0.2, fill_color=BLUE, stroke_width=2)
        self.play(DrawBorderThenFill(triangles), run_time=2, lag_ratio=.1)

        self.wait(2)
# }}}
# Trig {{{1
from manim.mobject.geometry.tips import ArrowTriangleTip,\
                                        ArrowSquareTip, ArrowSquareFilledTip,\
                                        ArrowCircleTip, ArrowCircleFilledTip
class Trigs(Scene):
    my_tex = TexTemplate()
    my_tex.add_to_preamble(r"\usepackage{mathrsfs}")
    # custom_tex_template = TexTemplate()
    # custom_tex_template.add_to_preamble(r"\usepackage[Dunhill]lmodern}")
    # MathTex.set_default(tex_templates=custom_tex_template)
    def construct(self):
        Dot.set_default(radius=0.08)
        # def CurcularArrow(obj, radius):
            # c = Circle(radius=radius)
            # arrow = ArrowTip().move_to(c.get_center())
            # shape = VGroup(c, arrow).move_to(obj.get_center())
            # return shape
        _a = Text("A", font_size=40).shift((LEFT+UP)*2)
        _b = Text("B", font_size=40).shift((RIGHT+UP)*2)
        self.add(_a, _b)
        arc_a = Arc(angle=335*DEGREES, start_angle=115*DEGREES).add_tip(tip_length=0.5, tip_shape=ArrowTriangleTip)
        self.add(arc_a.surround(_a, buff=0.6))
        arc_b = Arc(angle=335*DEGREES, start_angle=115*DEGREES).add_tip(tip_length=0.5, tip_shape=ArrowTriangleTip)
        self.add(arc_b.surround(_b, buff=0.6))


        cords = [[-0.5, 0, 0], [-2.5, 0, 0], [-1, 1, 0]]
        trig1 = Polygon(*cords, stroke_color=BLUE, fill_opacity=0.5, stroke_width=4).next_to(_a, DOWN*3)
        trig2 = trig1.copy().set_style(fill_opacity=0).next_to(_b, DOWN*3)
        dots1 = VGroup(*[Dot(point=i) for i in trig1.get_anchors()])
        dots2 = VGroup(*[Dot(point=i) for i in trig2.get_anchors()])
        self.add(dots1, dots2)
        self.play(DrawBorderThenFill(trig1))
        self.play(Create(trig2))
        self.wait(3)
# }}}
# MultipleTrigs {{{1
class MultipleTrigs(Scene):
    STROKE_WIDTH = 1.5
    ANGLE = 140
    def construct(self):
        def create_angle(pos, length, org):
            Line.set_default(stroke_width=self.STROKE_WIDTH)
            Dot.set_default(radius=0.035)
            Angle.set_default(radius=0.18, stroke_width=self.STROKE_WIDTH)
            Arc.set_default(stroke_width=self.STROKE_WIDTH)

            line1 = Line(org, [i * length for i in org])
            line2 = Line(org, [i * length + UP*0.01 for i in org])
            dot_origin = Dot(point=line1.get_start())
            dot1 = Dot(point=line1.get_end())
            dot2 = Dot(point=line2.get_end())
            dot2.add_updater(lambda x: x.move_to(line2.get_end()))
            angle = Angle(line1, line2)
            angle.add_updater(lambda x: x.become(Angle(line1, line2)))
            arc = ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=line1.get_length())
            arc.add_updater(lambda x: x.become(ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=line1.get_length())))
            cords = [i*(self.ANGLE/pos)*DEGREES for i in range(pos+1)]
            ##########
            # POINTS
            ##########
            c = Circle(stroke_opacity=0, radius=line1.get_length()).move_to(dot_origin.get_center())
            dots = VGroup(*[Dot(point=c.point_at_angle(i)) for i in cords])
            trigs = VGroup(*[Polygon(
                dot_origin.get_center(),
                c.point_at_angle(cords[i]),
                c.point_at_angle(cords[i+1]),
                ).set_style(stroke_color=BLUE, fill_opacity=0.2, fill_color=BLUE, stroke_width=self.STROKE_WIDTH)
                for i in range(pos)])
            self.add(c)


            self.add(line1, line2, dot_origin, dot1, dot2, angle, arc)
            self.add(Text("%s" %(pos), font_size=25, font="TiroDevanagariSanskrit").next_to(dot_origin, UP*6.5))

            # ANIMATION

            # self.play(FadeIn(dot_origin), 
                    # Rotate(line2, about_point=dot_origin.get_center(), angle=self.ANGLE*DEGREES), 
                    # DrawBorderThenFill(trigs),
                    # FadeIn(dots),
                    # run_time=2, lag_ratio=1)
            return [dot_origin, line2, trigs, dots]
            
        a1, b1, c1, d1 = create_angle(1, 2.3, [1, 0, 0])
        # a2, b2, c2, d2 = create_angle(2, 2.3, LEFT*2)
        # # a3, b3, c3, d3 = create_angle(3, 2.3, ORIGIN)
        # a4, b4, c4, d4 = create_angle(4, 2.3, RIGHT*2)
        # a5, b5, c5, d5 = create_angle(5, 2.3, RIGHT*4)
        self.play(
                AnimationGroup(
                FadeIn(a1),
                Rotate(b1, about_point=a1.get_center(), angle=self.ANGLE*DEGREES),
                DrawBorderThenFill(c1),
                FadeIn(d1)
                ),
                )
        self.wait()
# }}}
