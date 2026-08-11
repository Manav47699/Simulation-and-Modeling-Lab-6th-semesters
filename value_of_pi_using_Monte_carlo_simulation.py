import matplotlib.pyplot as plt
import numpy as np

# Total number of random samples (tweaked to give a slightly distinct estimate)
N = 1500000

# Generating random points in [0, 1] x [0, 1] region
coords = np.random.rand(N, 2)
x_vals = coords[:, 0]
y_vals = coords[:, 1]

# Condition check: point lies inside the unit quarter circle if distance <= 1
inside_mask = (x_vals**2 + y_vals**2) <= 1.0

# Estimating pi
pi_estimate = 4.0 * np.count_nonzero(inside_mask) / N

print(f"Estimated value of pi: {pi_estimate}")
print(f"Actual value of pi: {np.pi}")

# Visualization (subsampling points for efficient rendering)
plt.figure(figsize=(8, 8))
plt.scatter(
    x_vals[inside_mask],
    y_vals[inside_mask],
    color="red",
    s=1,
    label="Inside Circle",
)
plt.scatter(
    x_vals[~inside_mask],
    y_vals[~inside_mask],
    color="blue",
    s=1,
    label="Outside Circle",
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Monte Carlo Estimation of pi\nEstimated pi = {pi_estimate:.4f}")
plt.legend(loc="upper right")
plt.axis("equal")
plt.grid(True)
plt.show()