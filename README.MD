# `Spring`

A simple Python class to crate physics-like spring diagrams and draw them both in Matplotlib figures and PyGame surfaces.

## Usage

To create a spring, use, for example:

```python
spring = Spring(xy1=(1.0, 1.0),
                xy2=(4.0, 3.0),
                n_loops=5,
                loop_width=0.5,
                base_fraction=0.1)
```

The preceding code will create a spring with the origin at `xy1=(1.0, 1.0)` and the tip at `xy2=(4.0, 3.0)`, `n_loops=5` loops, each of width `loop_width=0.5` and a base fraction (length without loops) of `base_fraction=0.1` of the total spring length.

To draw this spring in a Matplotlib axis stored in `ax`, with color `color=blue` and line width `lw=2.0`, use:

```python
spring.draw_mpl(ax=ax, color="blue", lw=2.0)
```

To draw this spring in a PyGame surface stored in `surf`, with color `color=gold1` and line width `lw=2`, use:

```python
spring.draw_pyg(surface=surf, color="gold1", lw=2)
```

Also, check the two examples in the `examples` directory.

## Screenshots

<p align="center">
    <img src="https://i.imgur.com/KfyY3fM.png", width=350>
    <p align="center">An example image using Matplotlib.</p>
</p>

<p align="center">
    <img src="https://i.imgur.com/8uwRlAP.png", width=350>
    <p align="center">An example image using PyGame.</p>
</p>