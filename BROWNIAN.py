# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 03:08:24 2024

@author: samri
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

num_particles = 50
num_steps = 1000
step_size = 0.1

positions = np.zeros((num_particles, 2))

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
particles, = ax.plot([], [], 'bo', ms=6)

def update(frame):
    global positions
    positions += np.random.randn(num_particles, 2) * step_size
    particles.set_data(positions[:, 0], positions[:, 1])
    return particles,

ani = FuncAnimation(fig, update, frames=num_steps, interval=50, blit=True)

plt.title('Brownian Motion Simulation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
