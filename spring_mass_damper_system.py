import matplotlib.pyplot as plt
import numpy as np

# System Parameters (tweaked to create a unique output curve)
F = 6  # Force
W = 0.6  # Angular frequency (omega)
t0 = 0  # Initial time
T = 40  # Total time
dt = 0.01  # Time step

N = int((T - t0) / dt)
t = np.arange(0, N) * dt


# State derivative function: du/dt = [velocity, acceleration]
def model_derivatives(u_state, z_ratio):
    x, v = u_state[0], u_state[1]
    d_x = v
    d_v = (W**2) * (F - x) - 2 * z_ratio * W * v
    return np.array([d_x, d_v])


damping_ratios = [-0.15, 0.02, 1, 1.8]
line_styles = ["-", "--", "-.", ":"]

plt.figure(figsize=(10, 6))

for idx, z in enumerate(damping_ratios):
    u = np.zeros((N, 2))  # u[:, 0] = displacement, u[:, 1] = velocity
    u[0] = [0.0, 0.0]  # Initial state

    # RK4 Integration
    for i in range(N - 1):
        curr_u = u[i]
        m1 = model_derivatives(curr_u, z)
        m2 = model_derivatives(curr_u + 0.5 * dt * m1, z)
        m3 = model_derivatives(curr_u + 0.5 * dt * m2, z)
        m4 = model_derivatives(curr_u + dt * m3, z)

        u[i + 1] = curr_u + (dt / 6.0) * (m1 + 2 * m2 + 2 * m3 + m4)

    plt.plot(
        t,
        u[:, 0],
        label=f"z = {z}",
        linestyle=line_styles[idx % len(line_styles)],
    )

plt.xlabel("Time (s)")
plt.ylabel("Displacement x(t) (m)")
plt.title("Spring-Mass-Damper System Response")
plt.grid(True)
plt.legend()
plt.show()