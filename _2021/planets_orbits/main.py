from manim import *
import random


class PlanetOrbits(Scene):

    _red = "#cc241d"
    _white = "#fff4d8"
    _bg = "#020420"

    def construct(self):
        self.camera.background_color = self._bg
        Circle.set_default(stroke_width=1)
        stars = VGroup(*[
            Dot(radius=random.uniform(0.01, 0.03), fill_opacity=0.5).set_x(
                random.randint(-5, 4)).set_y(random.randint(-5, 4))
            for i in range(20)
        ])
        # Info {{{1
        # 
        # Data from: https://spaceplace.nasa.gov/
        # ---------------------------------------
        # "Mercury":    88
        # "Venus":      225
        # "Earth":      365
        # "Mars":       687
        # "Jupiter":    4333
        # "Saturn":     10759
        # "Uranus":     30687
        # "Neptune":    60190
        planets = {
                # name      0:days, 1:speed ratio(365/days), 2: position, 3:size, 
            "Mercury": [88, 4.15, 1, 0.08],
            "Venus": [225, 1.625, 1, 0.16],
            "Earth": [365, 1, 1, 0.3],
            "Mars": [687, 0.55, 1, 0.11],
            "Jupiter": [4333, 0.067, 1, 0.16],
            "Saturn": [10759, 0.035, 1, 0.15],
            "Uranus": [30687, 0.015, 1, 0.2],
            "Neptune": [60190, 0.006, 1, 0.1]
        }
        times = {
                # name      0:playing speed, 1:time to generate the shape
            "Mercury": [1, 80],
            "Venus": [1, 30],
            "Earth": [1],
            "Mars": [6, 80],
            "Jupiter": [10, 200],
            "Saturn": [10, 200],
            "Uranus": [10, 80],
            "Neptune": [10, 50]
        }
            # }}}
        # Icons {{{1
        icons = {
            "Sun": "./planets/sun.png",
            "Mercury": "./planets/mercury.png",
            "Venus": "./planets/venus.png",
            "Earth": "./planets/earth.png",
            "Mars": "./planets/mars.png",
            "Jupiter": "./planets/jupiter.png",
            "Saturn": "./planets/saturn.png",
            "Uranus": "./planets/uranus.png",
            "Neptune": "./planets/neptune.png"
        }

        # }}}
        # dot between {{{1
        def dot_between(obj1, obj2):
            # planet is a list of:
            # 0: planet name, 1: circle surround the planet, 2: planet path, and the 3: obj(icon of the planet)
            # assing the two circle to planet1, planet2
            planet1, planet2 = obj1[1], obj2[1]
            # Draw a hidden line between the two circles
            line = Line(start=planet1.get_center(),
                        end=planet2.get_center(),
                        stroke_opacity=0)

            # Make the line track the two circles
            line.add_updater(lambda x: x.put_start_and_end_on(
                planet1.get_center(), planet2.get_center()))

            # Put a dot and the midpoint of the line
            dot = Dot(radius=0.04, color=WHITE).add_updater(
                lambda x: x.move_to(line.get_midpoint()))
            # Adding line and dot to the scene
            self.add(line, dot)
            # Tracing the center of the dot 
            trace = TracedPath(dot.get_center, stroke_color=[RED_E, YELLOW_E, GREEN_E, TEAL_E, BLUE_D, PURPLE_E])
            # Adding the trace to the scene
            self.add(trace)
            return [trace, dot]
            # }}}

        # add planet {{{1
        def add_planet(planet):
            # tracking an image is tricky, it changes in size during moving, and that affect the position of the `tracking point`
            # --> which affect the trace 
            # Solution: I used a circle that surround the obj(icon), and I track the circle instead.
            # obj(icon of the planet) follow the circle using updaters
            circle = Circle(radius=planets[planet][3], stroke_opacity=0).move_to(
                UP * planets[planet][2]).scale(planets[planet][3])

            obj = ImageMobject(icons[planet]).scale(planets[planet][3]).add_updater(lambda x: x.move_to(circle.get_center()))

            planet_path = DashedVMobject(Circle(radius=planets[planet][2],
                                 stroke_color=GRAY,
                                 stroke_opacity=0.4),
                                 dashed_ratio=0.7,
                                 num_dashes=100,
                                 )

            self.play(AnimationGroup(FadeIn(
                planet_path, circle
                )), FadeIn(obj))
            return [planet, circle, planet_path, obj]
            # }}}
            # remove planet {{{1
        # TODO: A better way for cleaning the scene
        # def clean_scene(planet1, planet2): for example
        def remove_planet(planet):
            """
            Function for removing a planet from the scene
            PLANET is a list of:
            0: planet name, 1: circle surround the planet, 2: planet path, and the 3: obj(icon of the planet)
            """
            circle, planet_path, obj = planet[1], planet[2], planet[3]
            self.play(AnimationGroup(
                FadeOut(planet_path, circle), run_time=0.7),
                FadeOut(obj), run_time=0.7)
                # }}}
        # rotate planet {{{1
        def rotate_planet(planet):
            '''
            Function for rotating a planet
            PLANET is a list of:
            0: Planet name, 1: Circle that surround the icon
            list = [planet name, circle, planet path, obj(icon)]

            '''
            name, obj = planet[0], planet[1]
            obj.add_updater(lambda x, dt: x.rotate(2 * dt * planets[name][1], about_point=ORIGIN))
            # }}}

        sun = ImageMobject(icons["Sun"]).scale(0.2)
        self.add(sun, stars)
        # initialize the list of shapes
        list_of_shapes = VGroup()
        for plnt in ["Mercury", "Venus", "Mars"]:

        # for plnt in ["Mercury", "Venus", "Mars", "Neptune", "Saturn", "Jupiter"]:
            # If the planet was "farther" compared to Earth, it would take position 3 and Earth would take position 2.
            # Otherwise, planet = position 2, Earth = position 3.
            # change the dictionary to list for better indexing
            self.next_section("Start of section '%s'" %(plnt))
            temp_planets = planets
            if list(temp_planets.keys()).index(plnt) < list(temp_planets.keys()).index("Earth"):
                planets[plnt][2] = 2
                planets["Earth"][2] = 3
            else:
                planets[plnt][2] = 3
                planets["Earth"][2] = 2
            # retrieve time 
            time_to_generate_shape = times[plnt][1]
            other = add_planet(plnt)
            earth = add_planet("Earth")
            self.wait()
            rotate_planet(other)
            rotate_planet(earth)
            trace = dot_between(earth, other)
            self.wait(time_to_generate_shape)
            self.remove(trace[1])
            trace[0].clear_updaters()
            # self.play(trace[0].animate.scale(0.3).to_edge(planets[plnt][4], buff=1))
            self.play(FadeOut(trace[0]))
            # Prepare
            trace[0].scale(0.3)
            caption = Text("%s - %s"%("Earth", plnt), font_size=20, font="Bai Jamjuree SemiBold").next_to(trace[0], DOWN, buff=MED_SMALL_BUFF)
            shape = VGroup(trace[0], caption)
            list_of_shapes.add(shape)
            [remove_planet(i) for i in [earth, other]]
        self.play(FadeOut(sun), rune_time=0.2)
        self.wait(0.5)
        if len(list_of_shapes) <= 4:
            list_of_shapes.arrange_in_grid(rows=1, buff=1).move_to(ORIGIN)
            self.play(AnimationGroup(FadeIn(list_of_shapes), lag_ratio=0.3, run_time=3))
        else:
            list_of_shapes.arrange_in_grid(rows=2, buff=0.5).to_edge(UP, buff=0.5)
            self.play(AnimationGroup(FadeIn(list_of_shapes, lag_ratio=0.5, run_time=3)))

        self.wait(2)
