from manim import *

class PoyntingRobertsonDrag(Scene):
    def construct(self):
        # Create the Sun (central star)
        sun = Dot(color=YELLOW).scale(2)
        sun_label = Text("Sun").next_to(sun, UP)

        # Create the orbiting dust particle
        orbit_radius = 3
        dust_particle = Dot(color=WHITE).move_to([orbit_radius, 0, 0])
        dust_label = Text("Dust Particle").next_to(dust_particle, UP)
        
        # Circular orbit around the sun
        orbit = Circle(radius=orbit_radius, color=BLUE, stroke_opacity=0.5)
        
        # Arrows for forces
        gravity_arrow = Arrow(dust_particle.get_center(), sun.get_center(), buff=0, color=RED)
        radiation_arrow = Arrow(sun.get_center(), dust_particle.get_center(), buff=0, color=GREEN)
        pr_drag_arrow = Arrow(dust_particle.get_center(), [orbit_radius * 0.9, 0, 0], buff=0, color=ORANGE)
        
        # Labels for forces
        gravity_label = Text("Gravity", color=RED).next_to(gravity_arrow, LEFT)
        radiation_label = Text("Radiation Pressure", color=GREEN).next_to(radiation_arrow, RIGHT)
        pr_drag_label = Text("P-R Drag", color=ORANGE).next_to(pr_drag_arrow, DOWN)
        
        # Animate the appearance
        self.play(FadeIn(sun, sun_label))
        self.play(Create(orbit), FadeIn(dust_particle, dust_label))
        
        # Show the forces
        self.play(GrowArrow(gravity_arrow), Write(gravity_label))
        self.play(GrowArrow(radiation_arrow), Write(radiation_label))
        
        # Show P-R drag force
        self.play(GrowArrow(pr_drag_arrow), Write(pr_drag_label))
        
        # Animate the dust particle's decaying orbit
        self.wait(2)
        for i in range(5):
            orbit_radius *= 0.85
            self.play(dust_particle.animate.move_to([orbit_radius, 0, 0]), run_time=2)
            new_orbit = Circle(radius=orbit_radius, color=BLUE, stroke_opacity=0.5)
            self.play(Transform(orbit, new_orbit))
            self.wait(1)