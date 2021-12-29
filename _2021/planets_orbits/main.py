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
        #
        planets = {
            # name      days, speed ratio, distance, size
            "Mercury": [88, 365 / 88, 0.3, 0.08],
            "Venus": [225, 1.625, 2, 0.16],
            "Earth": [365, 365 / 365, 3, 0.3],
            "Mars": [687, 365 / 687, 1.5, 0.11],
            "Jupiter": [4333, 365 / 4333, 2, 0.06],
            "Saturn": [10759, 365 / 10759, 2.4, 0.15],
            "Uranus": [30687, 365 / 30687, 3, 0.2],
            "Neptune": [60190, 365 / 60190, 3.7, 0.1]
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
            trace = TracedPath(dot.get_center)
            # Adding the trace to the scene
            self.add(trace)
            return [trace, dot]
            # }}}

        # add planet {{{1
        def add_planet(planet):
            # tracking an image is tricky, it changes in size during moving, and that effect the position of tracking point
            # which affect the trace that it draw
            # Solution: I used a circle instead that surround the obj(icon), and I track the circle instead.
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
        def remove_planet(planet):
            # planet is a list of:
            # 0: planet name, 1: circle surround the planet, 2: planet path, and the 3: obj(icon of the planet)
            obj, circle, planet_path = planet[3], planet[1], planet[2]
            self.play(AnimationGroup(FadeOut(
                planet_path, circle
                )),
                FadeOut(obj)
                )
                # }}}
        # rotate planet {{{1
        def rotate_planet(planet, speed):
            # planet is a list of:
            # 0: Planet name, 1: Circle that surround the icon
            # Whole list [planet name, circle, planet path, obj(icon)]
            name, obj = planet[0], planet[1]
            obj.add_updater(lambda x, dt: x.rotate(2 * dt * speed * round(
                planets[name][1], 3), about_point=ORIGIN))
            # }}}

        sun = ImageMobject(icons["Sun"]).scale(0.2)
        self.add(sun, stars)
        venus = add_planet("Venus")
        earth = add_planet("Earth")
        self.wait()
        rotate_planet(venus, 1)
        rotate_planet(earth, 1)
        venus_earth = dot_between(earth, venus)

        self.wait(37)
        remove_planet(earth)
        remove_planet(venus)
        self.wait(2)
