from manim import *

class CoolAnimation(Scene):
    def construct(self):
        # Create objects
        square = Square(color=RED).shift(LEFT * 2)
        circle = Circle(color=BLUE).shift(RIGHT * 2)
        triangle = Triangle(color=GREEN).shift(DOWN * 2)

        # Display all shapes
        self.play(Create(square), Create(circle), Create(triangle))
        self.wait(1)

        # Rotate all together
        self.play(
            square.animate.rotate(PI),
            circle.animate.rotate(-PI),
            triangle.animate.rotate(PI / 2),
            run_time=2
        )
        self.wait(1)

        # Move all to center while changing color and scaling
        self.play(
            square.animate.move_to(ORIGIN).scale(1.5).set_color(ORANGE),
            circle.animate.move_to(ORIGIN).scale(0.5).set_color(PURPLE),
            triangle.animate.move_to(ORIGIN).scale(2).set_color(YELLOW),
            run_time=3
        )
        self.wait(1)

        # Write a formula after shapes merge
        formula = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}").scale(1.5)
        self.play(Write(formula))
        self.wait(3)
