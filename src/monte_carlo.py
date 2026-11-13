from synthetic_data import generate_measurements
from parameter_estimation import estimate_tau


def run_monte_carlo(t, m_true, A, omega, sigma, n_simulation = 100, seed = 42):
    tau_estimates = []
    for i in range(n_simulation):
        measured_data = generate_measurements(m_true, sigma, seed + i)
        tau_estimate, minimum_error = estimate_tau(t, measured_data, A, omega)
        
        tau_estimates.append(tau_estimate)
        
    return tau_estimates    
        
        
        
        
        
        
    