from manim import *

class RadialGradientDisk(Scene):
    def construct(self):
        # Load the radial gradient image
        gradient_image = ImageMobject("RadialGradientDisk.png")
        gradient_image.scale(1)  # Scale to desired size

        # Optionally, create a circular mask to restrict to a circular shape
        circle_mask = Circle(radius=1, color=WHITE, fill_opacity=0)
        gradient_image.set_opacity(1)  # Set full opacity for the image
        
        # Add temperature labels
        high_temp_label = Text("High Temperature", font_size=24, color=BLACK).next_to(gradient_image, ORIGIN, buff=0.5)
        low_temp_label = Text("Low Temperature", font_size=24, color=BLUE).next_to(gradient_image, RIGHT, buff=0.5)

        # Display the gradient disk and labels
        self.play(FadeIn(gradient_image), Write(high_temp_label), Write(low_temp_label))
        self.wait(2)
