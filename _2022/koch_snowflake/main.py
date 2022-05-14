from manim import *
import random

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 320*6
config.pixel_width = 180*6
config.frame_rate = 60

config.background_color = "#455D3E"

class SemiCrystalline(Scene):
    __dot_radius = 0.06
    __dot_color = RED_C
    font_size = 35
    def construct(self):
        hexagon = RegularPolygon(n=6, color=WHITE).scale(4)
        self.play(Create(hexagon))
        inst = Paragraph(
                "1. Pick a random point in the haxagon",
                "2. Pick a random edge and form a triangle",
                "3. Find the incenter of the triangle",
                font="Bitter",
                line_spacing=0.75,
                font_size=self.font_size
                ).to_corner(UR)
        def create_polygon(_start, speed):
            _verticies = hexagon.get_vertices()
            _num = random.randint(0, 5)
            _edge1 = _verticies[_num]
            _edge2 = _verticies[(_num+1)%6]
            _line1 = Line(start=_start, end=_edge1)
            _line2 = Line(start=_start, end=_edge2)
            _polygon = Polygon(_start, _edge1, _edge2, color=self.__dot_color)
            self.play(Create(_line1), Create(_line2), run_time=speed)
            self.play(FadeIn(_polygon),FadeOut(_line1, _line2), run_time=speed)
            _center = Dot(point=_polygon.get_center_of_mass(), radius=self.__dot_radius, color=self.__dot_color)
            self.play(FadeIn(_center), FadeOut(_polygon), run_time=speed)
            return _center, _polygon.get_center_of_mass()


        _start = [2, 1, 0]
        __points = 0
        __pattern = VGroup()
        # __dot = create_polygon(_start, 1)
        # self.play(Write(inst[0].next_to(__dot[0], DOWN, buff=0.5)))
        self.play(Write(inst[0].to_edge(UP, buff=0.5)))
        self.play(FadeOut(inst[0]))
        self.play(Write(inst[1].to_edge(UP, buff=0.5)))
        _start = __dot[1]
        __pattern.add(__dot[0])

        # for i in range(2):
            # __dot = create_polygon(_start, 0.1)
            # _start = __dot[1]
            # __points = __points + i
            # __pattern.add(__dot[0])
        # for i in range(10):
            # __dot = create_polygon(_start, 0.05)
            # _start = __dot[1]
            # __points = __points + i
            # __pattern.add(__dot[0])
        # for i in range(10):
            # __dot = create_polygon(_start, 0.03)
            # _start = __dot[1]
            # __points = __points + i
            # __pattern.add(__dot[0])

        __pattern.set_color(WHITE)
        self.wait(2)
