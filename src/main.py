import numpy as np
import matplotlib.pyplot as plt

from model import trap_center, solve_particle_motion

from synthetic_data import generate_measurements, generate_c

from parameter_estimation import estimate_tau

from monte_carlo import run_monte_carlo
from frequency_response import plot_frequency_response
from visualization import plot_particle_motion, plot_monte_carlo






t = np.linspace(0, 20, 80)

A = 1.0
omega = 1.0
tau_true = 2.0

c_true = trap_center(t, A, omega)
m_true = solve_particle_motion(t, tau_true, A, omega)


print("Trap positions:", c_true[:5])
print("Mean particle positions:", m_true[:5])

m_measured = generate_measurements(m_true, 0.05)
c_measured = generate_c(c_true, 0.05, seed=123)

print("Measured particle positions:", m_measured[:5])
print("Measured trap positions:", c_measured[:5])

tau_estimated, minimum_error = estimate_tau(t, m_measured, A, omega)
m_fitted = solve_particle_motion(t, tau_estimated, A, omega)

print(f"True relaxation time: {tau_true:.4f} s")
print(f"Estimated relaxation time: {tau_estimated:.4f} s")
print(f"Minimum squared error: {minimum_error:.6f} µm²")


tau_estimates = run_monte_carlo(
    t, m_true, A, omega,
    sigma=0.05,
    n_simulation=100,
    seed=42
)

print("Number of simulations:", len(tau_estimates))
print("Mean estimated tau:", np.mean(tau_estimates))
print("Standard deviation:", np.std(tau_estimates, ddof=1))

plot_particle_motion(t, c_true, m_true, m_measured, m_fitted)

if __name__ == "__main__":
    plot_particle_motion(t, c_true, m_true, m_measured, m_fitted)

    plot_monte_carlo(tau_estimates, tau_true)

    plot_frequency_response(tau_estimated)