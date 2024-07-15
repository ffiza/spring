import pygame
import sys
import numpy as np

from ..spring import Spring


class Animation:
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    COLOR_DEPTH: int = 32
    BACKGROUND: str = "gray15"
    FPS: int = 60
    SPRING_ANGULAR_VEL: float = 2.0
    SPRING_ELONGATION: int = 200
    DISPLAY_CAPTION: str = "Spring"

    def __init__(self) -> None:
        """
        The constructor for the Animation class.
        """
        pygame.init()
        self.running = True

        # Setup window
        self.screen = pygame.display.set_mode(
            size=(Animation.SCREEN_WIDTH, Animation.SCREEN_HEIGHT),
            flags=pygame.RESIZABLE, depth=Animation.COLOR_DEPTH)
        pygame.display.set_caption(Animation.DISPLAY_CAPTION)

        self.clock = pygame.time.Clock()
        self.time: float = 0.0

        self.spring = Spring(xy1=(400, 300),
                             xy2=(400 + Animation.SPRING_ELONGATION, 300),
                             n_loops=5, loop_width=15, base_fraction=0.1)

    @staticmethod
    def _quit() -> None:
        """
        This method quits the animation and closes the window.
        """
        pygame.quit()
        sys.exit()

    def _check_events(self) -> None:
        """
        Handle the events loop.
        """
        for event in pygame.event.get():
            # Quitting
            if event.type == pygame.QUIT:
                self._quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._quit()

            # Pause/Unpause
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.running = not self.running

    def _draw_elements(self) -> None:
        """
        Draw the elements on the screen.
        """

        self.spring.draw_pyg(surface=self.screen, color="gold1", lw=2)

    def _update_spring(self) -> None:
        x2 = (Animation.SPRING_ELONGATION + np.cos(
            Animation.SPRING_ANGULAR_VEL * self.time)) * np.cos(
                Animation.SPRING_ANGULAR_VEL * self.time)
        y2 = (Animation.SPRING_ELONGATION + np.cos(
            Animation.SPRING_ANGULAR_VEL * self.time)) * np.sin(
                Animation.SPRING_ANGULAR_VEL * self.time)
        self.spring.set_extremes(xy1=self.spring.xy1, xy2=(400 + x2, 200 + y2))

    def run(self) -> None:
        """
        Run the main animation loop.
        """

        while True:  # Main game loop
            self._check_events()
            self._update_spring()
            self.screen.fill(Animation.BACKGROUND)
            self._draw_elements()
            dt = self.clock.tick(Animation.FPS) / 1000
            self.time += dt
            pygame.display.flip()


if __name__ == "__main__":
    animation = Animation()
    animation.run()
