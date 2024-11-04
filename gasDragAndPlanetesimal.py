from manim import *

class GasDragAndPlanetesimalFormation(Scene):
    def construct(self):
        # Show a star and protoplanetary disk
        star = Dot(color=YELLOW).scale(2)
        disk = Annulus(inner_radius=0.5, outer_radius=4, color=BLUE, fill_opacity=0.2)
        self.play(FadeIn(star), FadeIn(disk))
        
        # Illustrate a small dust particle spiraling inward under linear drag
        dust_particle = Dot(color=WHITE).move_to([3, 0, 0])
        self.play(FadeIn(dust_particle))
        
        # Simulate inward migration under linear drag
        for i in range(10):
            self.play(dust_particle.animate.move_to([dust_particle.get_center()[0] * 0.9, 0, 0]), run_time=1)
        
        # Illustrate a larger particle experiencing quadratic drag (slower migration)
        large_particle = Dot(color=WHITE).move_to([3, 1, 0]).scale(1.5)
        self.play(FadeIn(large_particle))
        
        # Show slower inward migration due to quadratic drag
        for i in range(5):
            self.play(large_particle.animate.move_to([large_particle.get_center()[0] * 0.95, 1, 0]), run_time=1)
