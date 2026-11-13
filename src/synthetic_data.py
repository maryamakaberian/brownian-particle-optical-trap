import numpy as np


def generate_measurements(m_true, sigma, seed=42):
    rng = np.random.default_rng(seed)
    m_measurements = m_true + rng.normal(0, sigma, len(m_true))
    return m_measurements


def generate_c(c_true, sigma, seed = 123):
    rng = np.random.default_rng(seed)
    c_measurements = c_true + rng.normal(0, sigma, len(c_true))
    return c_measurements


    
    
     
    

    
    