from manim import *
import random

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 320*3
config.pixel_width = 180*3
config.frame_rate = 60

# # config.background_color = "#455D3E"
config.background_color = "#06070E"

class KochSnowflake(Scene):
    font_size = 35
    _white = "#f6e099"
    def construct(self):
        hexagon = RegularPolygon(n=6, color=self._white).scale(4)
        self.play(Create(hexagon))
        Dot.set_default(radius=0.06, color=self._white)
        hex_verticies = hexagon.get_vertices()
        __pattern = VGroup()

        # Tracking dots number
        dots = DecimalNumber(
                font_size=self.font_size,
                show_ellipsis=False,
                num_decimal_places=0).to_edge(DOWN).shift(LEFT)
        dots.add_updater(lambda d: d.set_value(len(__pattern)))
        ptxt = Text("points", font="Bitter", font_size=25).next_to(dots, RIGHT)
        ptxt.add_updater(lambda x: x.next_to(dots, RIGHT))
        self.play(AnimationGroup(FadeIn(dots, ptxt, shift=UP)), run_time=2)

        inst = Paragraph(
                "1. Pick a random point in the haxagon",
                "2. Pick a random edge and form a triangle",
                "3. Find the incenter of the triangle",
                "4. Repeat...",
                font="Bitter",
                line_spacing=0.75,
                disable_ligatures=True,
                font_size=self.font_size
                ).to_corner(UR).scale_to_fit_width(config.frame_width - 1).shift(RIGHT)



        rnd_dot = Dot(point=[2, 1, 0])

        __pattern.add(rnd_dot)
        self.play(FadeIn(rnd_dot), run_time=0.5)
        self.play(Flash(rnd_dot), Write(inst[0]))
        self.wait(0.5)
        _num = random.randint(0, 5)
        edge1, edge2 = hex_verticies[2], hex_verticies[3]
        _line1 = Line(start=[2, 1, 0], end=edge1, color=RED)
        _line2 = Line(start=[2, 1, 0], end=edge2, color=RED)
        polygon = Polygon([2, 1, 0], edge1, edge2, color=RED)
        self.play(Create(_line1), Create(_line2), Write(inst[1]), run_time=1.5)
        self.play(Create(polygon), FadeOut(_line1), FadeOut(_line2))
        _incenter = Dot(point=polygon.get_center_of_mass())
        _inner_line1 = Line(start=edge1, end=polygon.get_center_of_mass(), color=RED)
        _inner_line2 = Line(start=edge2, end=polygon.get_center_of_mass(), color=RED)
        _inner_line3 = Line(start=[2, 1, 0], end=polygon.get_center_of_mass(), color=RED)
        __pattern.add(_incenter)
        self.wait(0.5)
        self.play(Create(_inner_line1), Create(_inner_line2), Create(_inner_line3))
        self.play(FadeIn(_incenter), Write(inst[2]))
        self.play(AnimationGroup(FadeOut(polygon, _inner_line1, _inner_line2, _inner_line3)))
        self.wait(0.5)
        def create_polygon(_start, speed):
            _num = random.randint(0, 5)
            _edge1 = hex_verticies[_num]
            _edge2 = hex_verticies[(_num+1)%6]
            _line1 = Line(start=_start, end=_edge1)
            _line2 = Line(start=_start, end=_edge2)
            _polygon = Polygon(_start, _edge1, _edge2, color=RED)
            self.play(Create(_line1), Create(_line2), run_time=speed)
            _center = Dot(point=_polygon.get_center_of_mass())
            self.play(Create(_polygon))
            self.add(_center)
            self.remove(_polygon)
            self.remove(_line1, _line2)
            return _center, _polygon.get_center_of_mass()
        def create_incenter(_start, speed):
            _num = random.randint(0, 5)
            _polygon = Polygon(_start, hex_verticies[_num], hex_verticies[(_num+1)%6])
            _center = Dot(point=_polygon.get_center_of_mass())
            self.play(FadeIn(_center), run_time=speed)
            return _center, _polygon.get_center_of_mass()


        __points = 0
        __start = polygon.get_center_of_mass()

        self.play(Write(inst[3]))

        self.next_section()

        for i in range(3):
            __dot = create_polygon(__start, 0.5)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        self.next_section()
        for i in range(10):
            __dot = create_polygon(__start, 0.1)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        self.next_section()
        for i in range(3000):
            __dot = create_incenter(__start, 0.05)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        self.next_section()
        for i in range(5000):
            __dot = create_incenter(__start, 0.01)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        self.next_section()

        [x.scale(0.5) for x in __pattern]
        self.wait(2)
