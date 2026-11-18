import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from model import trap_center, solve_particle_motion
from synthetic_data import generate_measurements
from parameter_estimation import estimate_tau
from monte_carlo import run_monte_carlo


st.set_page_config(
    page_title="Brownian Particle Explorer",
    page_icon="🔬",
    layout="wide"
)

st.title("Brownian Particle in an Oscillating Optical Trap")
st.write(
    "Interactive simulation, relaxation-time estimation, "
    "and frequency-response analysis."
)

st.sidebar.header("Simulation Parameters")

A = st.sidebar.slider(
    'Trap amplitude(µm)',
    min_value =  0.1,
    max_value = 2.0,
    value = 1.0,
    step = 0.1
    
)

omega = st.sidebar.slider(
    "Angular frequency (rad/s)",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
    step=0.1
)

tau = st.sidebar.slider(
    "Relaxation time (s)",
    min_value=0.1,
    max_value=5.0,
    value=2.0,
    step=0.1
)

sigma = st.sidebar.slider(
    "Measurement noise σ (µm)",
    min_value=0.0,
    max_value=0.2,
    value=0.05,
    step=0.01
)

st.write(f"Trap amplitude: {A} µm")
st.write(f"Angular frequency: {omega} rad/s")
st.write(f"Relaxation time: {tau} s")

t = np.linspace(0, 20, 300)

c = trap_center(t, A, omega)
m = solve_particle_motion(t, tau, A, omega)

t = np.linspace(0, 20, 80)

c_true = trap_center(t, A, omega)

m_true = solve_particle_motion(t, tau, A, omega)

m_measured = generate_measurements(
    m_true,
    sigma,
    seed=42
)

tau_estimated, minimum_error = estimate_tau(
    t,
    m_measured,
    A,
    omega
)

m_fitted = solve_particle_motion(
    t,
    tau_estimated,
    A,
    omega
)

st.subheader("Relaxation Time Estimation")

col1, col2, col3 = st.columns(3)

col1.metric("True τ", f"{tau:.3f} s")
col2.metric("Estimated τ", f"{tau_estimated:.3f} s")
col3.metric(
    "Estimation error",
    f"{abs(tau_estimated - tau):.4f} s"
)


st.sidebar.divider()

st.sidebar.header("Choose Visualizations")

show_motion = st.sidebar.checkbox(
    "Particle Motion",
    value=True
)

show_monte_carlo = st.sidebar.checkbox(
    "Monte Carlo Histogram",
    value=False
)

show_frequency = st.sidebar.checkbox(
    "Frequency Response",
    value=False
)

if show_motion:
    st.subheader("Particle Motion and Parameter Estimation")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(t, c_true, label="Trap center", color="blue")
    ax.plot(t, m_true, label="True mean position", color="green")
    ax.plot(
        t, m_fitted,
        label="Fitted mean position",
        color="red",
        linestyle="--"
    )

    ax.scatter(
        t, m_measured,
        label="Synthetic measurements",
        color="orange",
        s=18,
        alpha=0.6
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Position (µm)")
    ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.02, 1),
    fontsize=10,
    frameon=True
)
    ax.grid(alpha=0.3)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    

if show_monte_carlo:
    st.subheader("Monte Carlo Analysis")

    n_simulations = st.slider(
        "Number of simulations",
        min_value=50,
        max_value=500,
        value=100,
        step=50
    )

    tau_estimates = run_monte_carlo(
        t,
        m_true,
        A,
        omega,
        sigma=sigma,
        n_simulation=n_simulations,
        seed=42
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.hist(
        tau_estimates,
        bins=15,
        alpha=0.7,
        edgecolor="white",
        label="Estimated relaxation times"
    )

    ax.axvline(
        tau,
        color="red",
        linestyle="--",
        label="True relaxation time"
    )

    ax.axvline(
        np.mean(tau_estimates),
        color="orange",
        linestyle=":",
        label="Mean estimated relaxation time"
    )

    ax.set_xlabel("Estimated relaxation time (s)")
    ax.set_ylabel("Number of simulations")
    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

    st.metric(
        "Mean estimated τ",
        f"{np.mean(tau_estimates):.4f} s"
    )

    st.metric(
        "Standard deviation",
        f"{np.std(tau_estimates, ddof=1):.4f} s"
    )    

if show_frequency:
    st.subheader("Frequency Response")

    omega_range = np.linspace(0.01, 5, 300)

    amplitude_ratio = 1 / np.sqrt(
        1 + (omega_range * tau_estimated)**2
    )

    phase_lag = np.degrees(
        np.arctan(omega_range * tau_estimated)
    )

    time_lag = (
        np.arctan(omega_range * tau_estimated)
        / omega_range
    )

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    axes[0].plot(omega_range, amplitude_ratio)
    axes[0].set_title("Amplitude Response")
    axes[0].set_ylabel("Particle / trap amplitude")

    axes[1].plot(omega_range, phase_lag)
    axes[1].set_title("Phase Lag")
    axes[1].set_ylabel("Degrees")

    axes[2].plot(omega_range, time_lag)
    axes[2].set_title("Time Lag")
    axes[2].set_ylabel("Seconds")

    for ax in axes:
        ax.set_xlabel("Angular frequency (rad/s)")
        ax.grid(alpha=0.3)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
