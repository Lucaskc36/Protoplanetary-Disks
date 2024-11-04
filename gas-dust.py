from manim import *

class GasDragEffect(Scene):
    def construct(self):
        # Add the star
        star = Dot(color=YELLOW).scale(2)
        self.play(FadeIn(star))
        
        # Dust particles in orbit
        dust_particles = VGroup(
            Dot(color=WHITE).move_to([3, 0, 0]),
            Dot(color=WHITE).move_to([3, 1, 0]),
            Dot(color=WHITE).move_to([3, -1, 0])
        )
        
        # Labels for gas drag
        drag_label = Text("Gas Drag", color=ORANGE).next_to(dust_particles[0], UP)
        
        # Add dust particles and drag label
        self.play(FadeIn(dust_particles))
        self.play(Write(drag_label))
        
        # Simulate drag force (particles moving inward)
        for i in range(5):
            new_positions = [
                dust_particles[0].get_center() * 0.95,
                dust_particles[1].get_center() * 0.95,
                dust_particles[2].get_center() * 0.95
            ]
            self.play(dust_particles.animate.move_to(new_positions[0]), run_time=1)
            self.wait(0.5)
