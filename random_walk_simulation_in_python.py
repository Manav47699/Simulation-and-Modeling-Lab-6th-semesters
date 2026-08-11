import random
import matplotlib.pyplot as plt
import numpy as np

# Simulation parameters (tweak step count, run count, and random seed)
Steps = 700
runs = 1200

# Set seed for reproducible results
random.seed(42)

final_positions = []
sample_path = [0]

# Perform multiple walk iterations
for run in range(runs):
    position = 0
    for step in range(Steps):
        # Update step direction based on probability cutoff
        if random.random() <= 0.5:
            position -= 1
        else:
            position += 1

        # Track trajectory of the initial run
        if run == 0:
            sample_path.append(position)

    final_positions.append(position)

# Statistical calculations
pos_array = np.array(final_positions)
mean_position = np.mean(pos_array)
rms_position = np.sqrt(np.mean(pos_array**2))
expected_rms = np.sqrt(Steps)

print("Mean Final Position:", round(mean_position, 4))
print("Measured RMS Position:", round(rms_position, 4))
print("Expected RMS Position:", round(expected_rms, 4))

# Plotting sample walk trajectories
plt.figure(figsize=(8, 5))

# Generate and plot visual trajectories for 10 representative walks
for walk in range(10):
    pos = 0
    path = [0]
    for step in range(Steps):
        if random.random() > 0.5:
            pos += 1
        else:
            pos -= 1
        path.append(pos)
    plt.plot(path)

plt.axhline(0, color="b", linestyle="-")
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("Random Walk Simulation")
plt.grid(True)
plt.show()