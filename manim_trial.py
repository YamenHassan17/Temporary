from manim import *

class MySimpleScene(Scene):
    def construct(self):
        square = Square(side_length=2, color=RED)
        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(square.animate.shift(RIGHT * 2))
        self.wait(2)
