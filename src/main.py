import numpy as np

from model import trap_center, solve_particle_motion

t = np.linspace(0, 20, 80)

A = 1.0
omega = 1.0
tau_true = 2.0

c_true = trap_center(t, A, omega)
m_true = solve_particle_motion(t, tau_true, A, omega)

print("Trap positions:", c_true[:5])
print("Mean particle positions:", m_true[:5])