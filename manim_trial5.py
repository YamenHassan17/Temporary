from manim import *

class NonMathShowcase(Scene):
    def construct(self):
        # Fireworks
        fireworks = VGroup(*[Dot(radius=0.05, color=random_bright_color()) for _ in range(20)])
        fireworks.arrange_in_grid(4, 5).move_to(ORIGIN)
        self.play(Create(fireworks))
        self.play(fireworks.animate.scale(3), run_time=2)
        self.play(FadeOut(fireworks))

        # Waves
        waves = VGroup(*[
            Circle(radius=0.5, color=BLUE).move_to(ORIGIN) for _ in range(5)
        ])
        for i, wave in enumerate(waves):
            wave.scale(1 + i * 0.5)
            wave.set_opacity(1 - i * 0.2)
        self.play(*[Create(wave) for wave in waves], run_time=1)
        self.play(*[wave.animate.scale(2).set_opacity(0) for wave in waves], run_time=2)
        self.play(FadeOut(waves))

        # Explosions
        explosion = VGroup(*[
            Line(ORIGIN, RIGHT * i, color=YELLOW).rotate(i * PI / 6) for i in range(12)
        ])
        self.play(Create(explosion))
        self.play(explosion.animate.scale(3).set_opacity(0), run_time=2)
        self.play(FadeOut(explosion))

        # Glowing trails
        trail = VGroup(*[
            Dot(radius=0.1, color=interpolate_color(RED, YELLOW, i / 10)) for i in range(10)
        ])
        for i, dot in enumerate(trail):
            dot.move_to(LEFT * (5 - i))
        self.play(*[Create(dot) for dot in trail], run_time=1)
        self.play(*[dot.animate.shift(RIGHT * 10) for dot in trail], run_time=2)
        self.play(FadeOut(trail))

        # Flying stars
        stars = VGroup(*[
            Star(color=random_bright_color()).scale(0.5).move_to(UP * 3 + LEFT * 6 + i * RIGHT * 1.5)
            for i in range(8)
        ])
        self.play(*[Create(star) for star in stars], run_time=1)
        self.play(*[star.animate.shift(DOWN * 6) for star in stars], run_time=2)
        self.play(FadeOut(stars))

        # Loading spinner
        spinner = Arc(radius=1, start_angle=0, angle=PI / 2, color=ORANGE).set_stroke(width=8)
        self.play(Create(spinner))
        self.play(Rotating(spinner, angle=PI * 8, about_point=ORIGIN), run_time=3)
        self.play(FadeOut(spinner))
