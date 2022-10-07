#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Dennis van Gils (https://github.com/Dennis-van-Gils)
# Inspiritation taken from https://www.youtube.com/watch?v=ZI1dmHv3MeM by https://www.youtube.com/c/TheCodingTrain

from matplotlib import pyplot as plt
from matplotlib import animation

import opensimplex

N_PIXELS = 256  # Number of pixels on a single axis
N_FRAMES = 50  # Number of time frames
FEATURE_SIZE = 24.0

# Generate noise
img_stack = opensimplex.polar_loop_2D_stack(
    N_pixels=N_PIXELS,
    N_frames=N_FRAMES,
    t_step=0.1,
    x_step=1 / FEATURE_SIZE,
    seed=3,
    verbose=True,
)

# Plot
fig_1 = plt.figure()
ax = plt.axes()
img = plt.imshow(
    img_stack[0],
    cmap="gray",
    vmin=-1,
    vmax=1,
    interpolation="none",
)
frame_text = ax.text(0, 1.02, "", transform=ax.transAxes)


def anim_init():
    img.set_data(img_stack[0])
    frame_text.set_text("")
    return img, frame_text


def anim_fun(j):
    img.set_data(img_stack[j])
    frame_text.set_text(f"frame {j:03d}")
    return img, frame_text


anim = animation.FuncAnimation(
    fig_1,
    anim_fun,
    frames=N_FRAMES,
    interval=40,
    init_func=anim_init,
    # blit=True,
)


plt.grid(False)
plt.axis("off")
plt.show()

anim.save("polar_loop_2D_stack.gif", dpi=69, writer="imagemagick", fps=25)