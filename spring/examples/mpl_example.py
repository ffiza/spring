import matplotlib.pyplot as plt

from ..spring import Spring


def plot_example() -> None:

    spring = Spring(xy1=(1.0, 1.0), xy2=(4.0, 3.0),
                    n_loops=5, loop_width=0.5, base_fraction=0.1)

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.tick_params(which='both', direction="in")
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls='-', lw=0.25, c="gainsboro")

    spring.draw_mpl(ax=ax, color="blue", lw=2.0)

    plt.show()


if __name__ == "__main__":
    plot_example()
