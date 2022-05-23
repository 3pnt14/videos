from manim import *
import random

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 320*6
config.pixel_width = 180*6
config.frame_rate = 60

config.background_color = "#455D3E"
class Sierpinski(Scene):
    def construct(self):
        Dot.set_default(radius=0.04)
        vertices = ([0,4,0],[4,-4,0],[-4,-4,0])
        triangle = Polygon(*vertices, stroke_color=WHITE)
        self.play(Create(triangle), run_time=2)
        self.wait(2)
        start_point = [1, 0.5, 0]
        dot = Dot(point=start_point)
        self.play(Create(dot))
        self.play(Flash(dot))
        self.wait(1)

        def create_line(pnt):
            line = Line(start=pnt, end=random.choice(vertices))
            return  line.get_center(), line
        points = []
        for i in range(3):
            center, line = create_line(start_point)
            # points.append(center)

            dot = Dot(point=center)
            self.play(Create(line))
            self.play(FadeIn(dot))
            self.play(FadeOut(line))
            start_point = center
        def cal_mid_point(start):
            end = random.choice(vertices)
            return [round((end[0]+start[0])/2, 3), round((end[1]+start[1])/2, 3),round((end[2]+start[2])/2, 3)]
        start = [1, 0.5, 0]
        for i in range(10000):
            pnt = cal_mid_point(start)
            start = pnt
            points.append(pnt)
            print(pnt)
        # self.add(*[Dot(point=s, radius=0.01) for s in points])
        self.play(AnimationGroup(*[FadeIn(Dot(point=s, radius=0.01)) for s in points]))
        self.wait(2)
