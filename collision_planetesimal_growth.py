from manim import *
class PlanetesimalFormation(Scene):
    def construct(self):
        # Initial dust particles
        small_particles = VGroup(
            Dot(color=WHITE).move_to([1.5, 0, 0]),
            Dot(color=WHITE).move_to([1.5, 1, 0]),
            Dot(color=WHITE).move_to([1.5, -1, 0])
        )
        
        # Larger body representing a planetesimal
        planetesimal = Dot(color=WHITE).scale(1.5).move_to([1, 0, 0])
        
        # Show small particles merging into a larger planetesimal
        self.play(FadeIn(small_particles))
        self.play(small_particles.animate.move_to(planetesimal.get_center()), FadeIn(planetesimal))
        
        # Final label
        label = Text("Planetesimal Formation").next_to(planetesimal, UP)
        self.play(Write(label))
        self.wait(2)