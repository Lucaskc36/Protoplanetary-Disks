from manim import *

class ProtoplanetaryDisk(Scene):
    def construct(self):
        # Create the star at the center
        star = Dot(color=YELLOW).scale(2)
        star_label = Text("Young Star").next_to(star, UP)
        
        # Create the protoplanetary disk as a circle of small particles
        disk = Annulus(inner_radius=0.5, outer_radius=3, color=BLUE, fill_opacity=0.2)
        disk_label = Text("Protoplanetary Disk").next_to(disk, UP)
        
        # Animate appearance
        self.play(FadeIn(star, star_label))
        self.play(FadeIn(disk, disk_label))
        self.wait(2)