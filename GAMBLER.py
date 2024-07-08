

import numpy as np
import matplotlib.pyplot as plt

def gamblers_ruin_simulation(initial_fortune, target_fortune, p, max_steps=1000):
    fortune = initial_fortune
    fortunes = [fortune]
    
    for _ in range(max_steps):
        if fortune == 0 or fortune == target_fortune:
            break
        bet_result = np.random.choice([-1, 1], p=[1-p, p])
        fortune += bet_result
        fortunes.append(fortune)
    
    return fortunes


n = int(input("Enter the number of simulations: "))
initial_fortune = int(input("Enter the initial fortune: "))
target_fortune = int(input("Enter the target fortune: "))
max_steps = int(input("Enter the maximum number of steps: "))
p = float(input("Enter the probability of winning each bet (less than 0.5 to be against the gambler): "))


all_fortunes = []
for _ in range(n):
    fortunes = gamblers_ruin_simulation(initial_fortune, target_fortune, p, max_steps)
    all_fortunes.append(fortunes)


plt.figure(figsize=(12, 8))
for fortunes in all_fortunes:
    plt.plot(fortunes, drawstyle='steps-post')

plt.xlabel('Time (Number of Bets)')
plt.ylabel('Fortune')
plt.title(f'Gambler\'s Ruin Simulation ({n} Simulations)')
plt.grid(True)
plt.show()
