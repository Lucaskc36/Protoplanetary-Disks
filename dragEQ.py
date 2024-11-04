from manim import *
class TitleAndEquation(Scene):
    def construct(self):
        # Create the title
        title = Text("Gas Drag", font_size=48).to_edge(UP)
        
        # Create the equation
        equation = MathTex(
            r"F_D" , r"=-{",  r"C_D", r"A", r"\rho_g", r"v^2", "\\over", "2}",  # Reference C_D within the fraction
            font_size=48
        )



        # Add title and equation to the scene
        self.play(Write(title))
        self.play(Write(equation))

        # Pause for a moment before moving the equation
        self.wait(2)

        equation.set_color_by_tex("C_D",YELLOW)
        # Move the equation to the upper left corner
        self.play(equation.animate.to_corner(UP + LEFT))
        # Make a copy of C_D to move to the origin
        c_d = equation.get_part_by_tex("C_D").copy()

        self.play(c_d.animate.move_to(ORIGIN))
        
        # Create a definition for C_D and position it next to the copy
        c_d_definition = Text(" = Drag Coefficient", font_size=36).next_to(c_d, RIGHT)
        # Group the two and display together
        c_d_def = VGroup(c_d, c_d_definition)
        ## WRITE AND MOVE at the same time (VERY AESTHETICALLY PLEASING)
        self.play(Write(c_d_definition),c_d_def.animate.move_to(ORIGIN))

        # Hold the final position for a moment
        self.wait(2)

        self.play(c_d_def.animate.to_corner(UR))
        self.play(c_d_definition.animate.set_color(YELLOW))

        self.wait(2)

        ############## C_D EXPLANATION HERE

        #### VARIABLE TRANSITION C_D -> A ####

        self.play(c_d_def.animate.set_color(WHITE))
        self.play(equation.animate.set_color_by_tex("C_D",WHITE))
        self.play(equation.animate.set_color_by_tex("A",YELLOW))

        ####### A duplicate and expand ########

        a = equation.get_part_by_tex("A").copy()
        self.play(a.animate.move_to(ORIGIN))
        a_definition = Text(" = Area of body", font_size=36).next_to(a, RIGHT)
        a_def = VGroup(a, a_definition)
        self.play(Write(a_definition),a_def.animate.move_to(ORIGIN))
        self.wait(2)

        ### Move to the top right offset by the C_D DEF

        self.play(a_def.animate.next_to(c_d_def, DOWN))
        self.play(a_def.animate.set_color(YELLOW))

        self.wait(2)

        ########### A EXPLANATION ########

        #### VARIABLE TRANSITION A -> RHO ####

        self.play(a_def.animate.set_color(WHITE))
        self.play(equation.animate.set_color_by_tex("A",WHITE))
        self.play(equation.animate.set_color_by_tex(r"\rho_g",YELLOW))
        
        ####### A duplicate and expand ########

        rho = equation.get_part_by_tex(r"\rho_g").copy()
        self.play(rho.animate.move_to(ORIGIN))
        rho_definition = Text(" = Gas Density", font_size=36).next_to(rho, RIGHT)
        rho_def = VGroup(rho, rho_definition)
        self.play(Write(rho_definition),rho_def.animate.move_to(ORIGIN))
        self.wait(2)

        ### Move below a_def DEF
        self.play(rho_def.animate.next_to(a_def, DOWN))
        self.play(rho_def.animate.set_color(YELLOW))

        self.wait(2)

        #### VARIABLE TRANSITION RHO -> v ####

        self.play(rho_def.animate.set_color(WHITE))
        self.play(equation.animate.set_color_by_tex(r"\rho_g",WHITE))
        self.play(equation.animate.set_color_by_tex(r"v^2",YELLOW))
        
        ####### A duplicate and expand ########

        v = equation.get_part_by_tex(r"v^2").copy()
        self.play(v.animate.move_to(ORIGIN))
        v_definition = Text(" = Velocity", font_size=36).next_to(v, RIGHT)
        v_def = VGroup(v, v_definition)
        self.play(Write(v_definition),v_def.animate.move_to(ORIGIN))
        self.wait(2)

        ### Move below rho_def DEF
        self.play(v_def.animate.next_to(rho_def, DOWN))
        self.play(v_def.animate.set_color(YELLOW))

        self.wait(2)


                                                                                                                                   



