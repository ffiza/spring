import numpy as np
import matplotlib.pyplot as plt
import pygame as pyg


class Spring:
    def __init__(self,
                 xy1: tuple[float, float],
                 xy2: tuple[float, float],
                 n_loops: int,
                 loop_width: float,
                 base_fraction: float) -> None:
        """
        A class to draw springs in Matplotlib or PyGame.

        Parameters
        ----------
        xy1 : tuple[float, float]
            The position of the tail of the spring.
        xy2 : tuple[float, float]
            The position of the head of the spring.
        n_loops : int
            The number of loops in the spring.
        loop_width : float
            The width of each loop.
        base_fraction : float
            The fraction of the total length corresponding to the base of the
            spring (the region with no loops).
        """
        self.xy1: np.Array
        self.xy2: np.Array
        self.length: float
        self.points: np.ndarray

        self.n_loops: int = n_loops
        self.loop_width: float = loop_width
        self.base_fraction: float = base_fraction

        self.set_extremes(xy1, xy2)

    def set_extremes(self, xy1: tuple[float, float],
                     xy2: tuple[float, float]) -> None:
        """
        Set the location of the origin (`xy1`) and the tip (`xy2`) of the
        spring.

        Parameters
        ----------
        xy1 : tuple[float, float]
            The location of the origin of the spring.
        xy2 : tuple[float, float]
            The location of the tip of the spring.
        """
        self.xy1 = np.array(xy1)
        self.xy2 = np.array(xy2)
        self.length = np.linalg.norm(self.xy2 - self.xy1)
        self._calculate_points()

    def _calculate_points(self) -> None:
        """
        Calculates all the points needed to draw the spring.
        """
        n_points = 3 + 4 * self.n_loops

        # Spring properties
        base_length = self.base_fraction * self.length
        loops_length = self.length - 2 * base_length
        loop_length = loops_length / self.n_loops
        dxy = (self.xy2 - self.xy1) / np.linalg.norm(self.xy2 - self.xy1)
        dxy_orth = np.array((-dxy[1], dxy[0]))

        self.points = np.nan * np.ones((n_points, 2))
        self.points[0] = self.xy1
        self.points[1] = self.xy1 + self.base_fraction * (self.xy2 - self.xy1)
        multipliers = [1, -1, -1, 1]
        j = 0
        for i in range(2, self.n_loops * 4 + 2):
            self.points[i] = self.points[i - 1] + dxy * loop_length / 4 \
                + multipliers[j] * dxy_orth * self.loop_width / 2
            j += 1
            if j > 3:
                j = 0
        self.points[-1] = self.xy2

    def draw_mpl(self,
                 ax: plt.Axes,
                 color: str = "black",
                 lw: float = 1.0) -> None:
        """
        Draw the spring on a Matplotlib axis.

        Parameters
        ----------
        ax : plt.Axes
            The axes on which to draw the spring.
        color : str, optional
            The color of the spring. "white" by default.
        lw : float, optional
            The line width. 1.0 by default.
        """
        ax.plot(self.points[:, 0], self.points[:, 1], lw=lw, color=color)

    def draw_pyg(self,
                 surface: pyg.Surface,
                 color: pyg.Color = pyg.Color(255, 255, 255, 255),
                 lw: int = 1) -> None:
        """
        Draw the spring on a PyGame surface.

        Parameters
        ----------
        surface : pyg.Surface
            The surface on which to draw the spring.
        color : pyg.Color, optional
            The color of the spring. White by default.
        lw : int, optional
            The line width. 1 by default.
        """
        pyg.draw.lines(surface=surface,
                       color=color,
                       closed=False,
                       points=self.points,
                       width=lw)
