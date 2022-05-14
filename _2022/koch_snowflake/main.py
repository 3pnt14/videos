from manim import *
import random

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 320*3
config.pixel_width = 180*3
config.frame_rate = 60

# config.background_color = "#455D3E"
config.background_color = "#06070E"

class KochSnowflake(Scene):
    # __dot_radius = 0.06
    # __dot_color = RED_C
    font_size = 35
    _white = "#f6e099"
    def construct(self):
        hexagon = RegularPolygon(n=6, color=self._white).scale(4)
        self.play(Create(hexagon))
        Dot.set_default(radius=0.02, color=self._white)
        hex_verticies = hexagon.get_vertices()
        __pattern = VGroup()
        inst = Paragraph(
                "1. Pick a random point in the haxagon",
                "2. Pick a random edge and form a triangle",
                "3. Find the incenter of the triangle",
                "4. Repeat...",
                font="Bitter",
                line_spacing=0.75,
                disable_ligatures=True,
                font_size=self.font_size
                ).to_corner(UR).scale_to_fit_width(config.frame_width - 2)



        rnd_dot = Dot(point=[2, 1, 0])
        __pattern.add(rnd_dot)
        self.play(FadeIn(rnd_dot), run_time=0.5)
        self.play(Flash(rnd_dot), Write(inst[0]))
        self.wait(0.5)
        _num = random.randint(0, 5)
        edge1, edge2 = hex_verticies[2], hex_verticies[3]
        _line1 = Line(start=[2, 1, 0], end=edge1)
        _line2 = Line(start=[2, 1, 0], end=edge2)
        polygon = Polygon([2, 1, 0], edge1, edge2, color=RED)
        self.play(Create(_line1), Create(_line2), Write(inst[1]), run_time=1.5)
        self.play(Create(polygon), FadeOut(_line1), FadeOut(_line2))
        _incenter = Dot(point=polygon.get_center_of_mass(), color=RED)
        __pattern.add(_incenter)
        self.wait(0.5)
        self.play(FadeIn(_incenter), Write(inst[2]))
        self.play(FadeOut(polygon))
        self.wait(0.5)
        def create_polygon(_start, speed):
            _num = random.randint(0, 5)
            _edge1 = hex_verticies[_num]
            _edge2 = hex_verticies[(_num+1)%6]
            _line1 = Line(start=_start, end=_edge1)
            _line2 = Line(start=_start, end=_edge2)
            _polygon = Polygon(_start, _edge1, _edge2, color=RED)
            self.play(Create(_line1), Create(_line2), run_time=speed)
            self.play(FadeIn(_polygon),FadeOut(_line1, _line2), run_time=speed)
            _center = Dot(point=_polygon.get_center_of_mass())
            self.play(FadeIn(_center), FadeOut(_polygon), run_time=speed)
            return _center, _polygon.get_center_of_mass()


        __points = 0
        __start = polygon.get_center_of_mass()
        print(__start)

        self.play(Write(inst[3]))
        # Tracking dots number
        dots = DecimalNumber(
                show_ellipsis=False,
                num_decimal_places=0).to_edge(DOWN)
        dots.add_updater(lambda d: d.set_value(len(__pattern)))
        ptxt = Text("points", font="Bitter", font_size=25).next_to(dots, RIGHT)
        self.add(dots, ptxt)
        for i in range(5):
            __dot = create_polygon(__start, 0.5)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        for i in range(50):
            __dot = create_polygon(__start, 0.3)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        for i in range(100):
            __dot = create_polygon(__start, 0.1)
            __start = __dot[1]
            __points = __points + i
            __pattern.add(__dot[0])
        for i in range(1845):
            __dot = create_polygon(__start, 0.01)

        # __pattern.set_color(WHITE)
        self.wait(2)
