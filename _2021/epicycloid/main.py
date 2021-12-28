from manim import *
import random


class Epicycloid(Scene):
    venus_dist = 2
    earth_dist = 3
    _bg = BLACK
    _red = "#cc241d"
    _white = "#fff4d8"
    _bg = "#020420"

    def construct(self):
        self.camera.background_color = self._bg

        sun = Circle(radius=0.35,
                     fill_color=YELLOW_E,
                     fill_opacity=1.0,
                     stroke_opacity=1,
                     stroke_width=1.5,
                     stroke_color=self._bg)
        venus = Circle(radius=0.1,
                       fill_color=YELLOW_B,
                       fill_opacity=1.0,
                       stroke_opacity=1,
                       stroke_width=1.5,
                       stroke_color=self._bg).move_to((UP+LEFT)*self.venus_dist)
        earth = Circle(radius=0.2,
                       fill_color=BLUE_E,
                       fill_opacity=1.0,
                       stroke_opacity=1,
                       stroke_width=1.5,
                       stroke_color=self._bg).move_to((UP+LEFT)*self.earth_dist)
        earth_path = Circle(radius=self.earth_dist,
                            stroke_width=1.5,
                            stroke_color=WHITE,
                            stroke_opacity=0.2)
        venus_path = Circle(radius=self.venus_dist,
                            stroke_width=1.5,
                            stroke_color=WHITE,
                            stroke_opacity=0.2)
        venus.shift(RIGHT * self.venus_dist)
        earth.shift(RIGHT * self.earth_dist)
        ve_path = Line(start=earth.get_center(),
                       end=venus.get_center(),
                       stroke_opacity=0)
        ve_path.add_updater(lambda x: x.put_start_and_end_on(
            earth.get_center(), venus.get_center()))

        middle_pnt = Dot(ve_path.get_midpoint(), radius=0.05)
        middle_pnt.add_updater(lambda x: x.move_to(ve_path.get_midpoint()))
        trace = TracedPath(middle_pnt.get_center)

        stars = VGroup(*[
            Dot(radius=random.uniform(0.01, 0.03), fill_opacity=0.5).set_x(
                random.randint(-5, 4)).set_y(random.randint(-5, 4))
            for i in range(20)
        ])
        self.add(stars, ve_path, earth_path, venus_path, earth, venus, sun)
        Text.set_default(font_size=17, font="monospace")
        sun_copy = sun.copy()
        earth_copy = earth.copy()
        venus_copy = venus.copy()
        legend = VGroup(sun_copy, earth_copy,
                        venus_copy).arrange(direction=DOWN,
                                            buff=0.5).scale(0.6).to_edge(UL)
        sun_txt = Text("Sun").next_to(sun_copy, RIGHT)
        venus_txt = Text("Venus").next_to(venus_copy,
                                            RIGHT).align_to(sun_txt, LEFT)
        earth_txt = Text("Earth").next_to(earth_copy,
                                          RIGHT).align_to(sun_txt, LEFT)

        def draw_epicycle(velocity, time):
            venus_velocity = velocity
            txt = Text("Speed ratio: %s" % (velocity),
                       font_size=25).to_edge(UP, buff=MED_SMALL_BUFF)
            self.play(FadeIn(txt))
            earth_rotate = lambda planet, dt: planet.rotate(
                2 * dt, about_point=sun.get_center())
            venus_rotate = lambda planet, dt: planet.rotate(
                2 * dt * venus_velocity, about_point=sun.get_center())
            earth.add_updater(earth_rotate)
            venus.add_updater(venus_rotate)
            trace_permanent = TracedPath(middle_pnt.get_center)
            trace_fade = TracedPath(middle_pnt.get_center, dissipating_time=0.4, stroke_opacity=[1, 0], stroke_color=self._red, stroke_width=3)
            self.add(trace_permanent, trace_fade, middle_pnt)
            self.wait(time)
            self.remove(trace_permanent, trace_fade, middle_pnt)
            self.play(FadeOut(txt))
        def glowing(x):
            x.set_style(fill_opacity=(dt*1))
            x.set_style(fill_opacity=(dt*0))


        # Animation
        ## Instruction

        self.play(FadeIn(legend), Write(sun_txt), Write(earth_txt),
                  Write(venus_txt))
        txt0 = Text("Write a line between the two planets.",
                    font_size=18).next_to(ve_path, UP * 2)
        self.play(Write(txt0),
                  Write(ve_path.set_style(stroke_opacity=1.0,
                                          stroke_width=1.5)),
                  run_time=1.5)
        self.wait(1)
        txt1 = Text("And then take it midpoint, and track it",
                    font_size=18).next_to(ve_path, UP * 2)
        self.play(ReplacementTransform(txt0, txt1),
                  FadeIn(middle_pnt),
                  run_time=1.5)
        self.play(ve_path.animate.set_style(stroke_opacity=0))
        planet_br = Brace(ve_path, direction=UP)
        txt2 = Text("The speed of the two planets differ.",
                    font_size=18).next_to(planet_br, UP * 0.7)

        txt4 = Text("the ratio between the two speeds",
                    font_size=18).next_to(planet_br, UP * 0.7)
        txt3 = Text("A `Speed ratio` indicator above shows",
                    font_size=18).next_to(txt4, UP)
        arrow = Arrow(start=txt3.get_center(),
                      end=(UP * 3.5 + LEFT * 0.5),
                      stroke_width=4)
        self.play(FadeOut(txt1))
        self.play(Write(planet_br), Write(txt2))
        self.wait(1)
        self.play(ReplacementTransform(txt2, VGroup(txt3, txt4)))
        self.play(GrowArrow(arrow, run_time=2))
        self.play(FadeOut(arrow))
        self.wait(1)
        self.play(FadeOut(VGroup(txt3, txt4, planet_br)))

        ## Simulation

        draw_epicycle(1.625, 40)
        self.wait(1)
