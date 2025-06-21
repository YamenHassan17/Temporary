from manim import *

class MySecondMathScene(Scene):
    def construct(self):
        circle = Circle(radius=1.5, color=BLUE)
        self.play(Create(circle))
        self.play(circle.animate.shift(LEFT*2))
        formula = MathTex(r"E=mc^2").scale(2)
        formula.move_to(RIGHT*2)
        self.play(Write(formula))
        self.wait(2)
