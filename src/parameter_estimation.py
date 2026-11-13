from scipy.optimize import minimize_scalar
import numpy as np
from model import trap_center, solve_particle_motion


def error_function(tau, t, measured_data, A, omega):
    prediction = solve_particle_motion(t, tau, A, omega) 
    residual = prediction - measured_data
    return np.sum(residual **2)


def estimate_tau(t, measured_data, A, omega):
    result = minimize_scalar(
        error_function,
        bounds=(0.1, 5),
        method="bounded",
        args=(t, measured_data, A, omega)
    )

    return result.x, result.fun







    
    
    