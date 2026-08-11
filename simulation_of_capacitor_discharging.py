import matplotlib.pyplot as plt
import numpy as np

# System Parameters
R = 1000  # Resistance in ohms
C = 0.0012  # Capacitance in farads
V0 = 12  # Initial voltage in volts
t0 = 0  # Start time
T = 12  # Total time in seconds
dt = 0.01  # Time step

# Generating time points
t = np.arange(t0, T + dt, dt)

# Initialize voltage list with initial condition
V = [V0]

# Numerical integration using Euler's method
for i in range(len(t) - 1):
    dV = -V[i] / (R * C)
    V.append(V[i] + dV * dt)

# Plotting the results
plt.figure(figsize=(8, 5))
plt.plot(t, V, color="blue", label="Capacitor Discharging")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Capacitor Discharging Simulation")
plt.grid(True)
plt.legend()
plt.show()