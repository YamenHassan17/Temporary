from manim import *

class BouncingBalls(Scene):
    def construct(self):
        # Create balls
        ball1 = Dot(color=RED).move_to(LEFT * 3 + DOWN * 2)
        ball2 = Dot(color=BLUE).move_to(RIGHT * 3 + DOWN * 2)

        self.play(Create(ball1), Create(ball2))
        self.wait(1)

        # Make them bounce up together
        for _ in range(3):
            self.play(
                ball1.animate.move_to(ball1.get_center() + UP * 2),
                ball2.animate.move_to(ball2.get_center() + UP * 3),
                run_time=0.5
            )
            self.play(
                ball1.animate.move_to(ball1.get_center() + DOWN * 2),
                ball2.animate.move_to(ball2.get_center() + DOWN * 3),
                run_time=0.5
            )

        # Make them spin around each other
        self.play(
            Rotating(ball1, angle=PI * 2, about_point=ORIGIN),
            Rotating(ball2, angle=PI * 2, about_point=ORIGIN),
            run_time=3
        )

        # Fade out
        self.play(FadeOut(ball1), FadeOut(ball2))
        self.wait(1)
