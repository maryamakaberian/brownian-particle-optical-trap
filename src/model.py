import numpy as np
from scipy.integrate import odeint


def trap_center(t, A, omega):
    """Return the position of the oscillating optical trap."""
    return A * np.sin(omega * t)


def relaxation(m, t, tau, A, omega):
    """Time derivative of the mean particle position."""
    return -(m - trap_center(t, A, omega)) / tau


def solve_particle_motion(t, tau, A, omega):
    """Solve the mean particle relaxation equation."""
    sol = odeint(
        relaxation,
        0.0,
        t,
        args=(tau, A, omega)
    )

    return sol[:, 0]

