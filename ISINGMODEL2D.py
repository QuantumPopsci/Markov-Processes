
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_lattice(N):
    return np.random.choice([-1, 1], size=(N, N))

def calculate_energy(lattice, J, h):
    N = lattice.shape[0]
    energy = 0
    for i in range(N):
        for j in range(N):
            S = lattice[i, j]
            neighbors = lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + lattice[(i-1)%N, j] + lattice[i, (j-1)%N]
            energy += -J * S * neighbors - h * S
    return energy / 2  # Each pair counted twice

def metropolis_step(lattice, J, h, beta):
    N = lattice.shape[0]
    for _ in range(N**2):
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)
        S = lattice[i, j]
        dE = 2 * S * (J * (lattice[(i+1)%N, j] + lattice[i, (j+1)%N] + lattice[(i-1)%N, j] + lattice[i, (j-1)%N]) + h)
        if dE < 0 or np.random.rand() < np.exp(-beta * dE):
            lattice[i, j] = -S
    return lattice

def simulate_ising(N, J, h, beta, steps):
    lattice = initialize_lattice(N)
    energy_list = []
    lattice_list = []
    for step in range(steps):
        lattice = metropolis_step(lattice, J, h, beta)
        energy = calculate_energy(lattice, J, h)
        energy_list.append(energy)
        lattice_list.append(lattice.copy())
    return energy_list, lattice_list

# Parameters
N = 20            # Lattice size (N x N)
J = 1.0           # Interaction strength
h = 0     # External magnetic field
T = 2        # Temperature
beta = 1.0 / T    # Inverse temperature
steps = 300      # Number of simulation steps
interval = 50     # Interval between frames in milliseconds


energy_list, lattice_list = simulate_ising(N, J, h, beta, steps)


fig, axs = plt.subplots(2, 1, figsize=(8, 8))
ax_energy = axs[0]
ax_lattice = axs[1]

line_energy, = ax_energy.plot([], [], lw=2)
ax_energy.set_xlim(0, steps)
ax_energy.set_ylim(min(energy_list) - 10, max(energy_list) + 10)
ax_energy.set_xlabel('Time step')
ax_energy.set_ylabel('Energy')
ax_energy.set_title('Energy Evolution in the Ising Model')


im = ax_lattice.imshow(lattice_list[0], cmap='coolwarm', animated=True)

def update(frame):
    im.set_array(lattice_list[frame])
    line_energy.set_data(range(frame + 1), energy_list[:frame + 1])
    return [im, line_energy]


ani = animation.FuncAnimation(fig, update, frames=range(steps), interval=interval, blit=True)

plt.tight_layout()
plt.show()
