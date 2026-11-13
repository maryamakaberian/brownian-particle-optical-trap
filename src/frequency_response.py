import numpy as np
import matplotlib.pyplot as plt


def plot_frequency_response(tau):

    omega = np.linspace(0.01, 5, 300)

    amplitude_ratio = 1 / np.sqrt(1 + (omega * tau)**2)
    phase_lag = np.degrees(np.arctan(omega * tau))
    time_lag = np.arctan(omega * tau) / omega

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    colors = ["#0077B6", "#E76F51", "#2A9D8F"]

    axes[0].plot(omega, amplitude_ratio, color=colors[0], linewidth=2.5)
    axes[0].set_title("Amplitude Response")
    axes[0].set_ylabel("Particle / trap amplitude")

    axes[1].plot(omega, phase_lag, color=colors[1], linewidth=2.5)
    axes[1].set_title("Phase Lag")
    axes[1].set_ylabel("Phase lag (degrees)")

    axes[2].plot(omega, time_lag, color=colors[2], linewidth=2.5)
    axes[2].set_title("Time Lag")
    axes[2].set_ylabel("Time lag (s)")

    for ax in axes:
        ax.set_xlabel("Angular frequency (rad/s)")
        ax.grid(alpha=0.25)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.suptitle(
        f"Frequency Response of a Brownian Particle | τ = {tau:.1f} s",
        fontsize=15,
        fontweight="bold"
    )

    fig.tight_layout()

    fig.savefig(
        "frequency_response.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()