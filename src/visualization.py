import matplotlib.pyplot as plt
import numpy as np



def plot_monte_carlo(tau_estimates, tau_true):
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.hist(
        tau_estimates,
        bins = 15, 
        alpha = 0.7,
        edgecolor="white",
        label="Monte Carlo estimates"
     )
    ax.axvline(
        tau_true,
        color="red",
        linestyle="--",
        linewidth=2,
        label="True relaxation time")
        
        
    ax.axvline(
        np.mean(tau_estimates),
        color = 'orange',
        linestyle = ':',
        linewidth = 2,
        label = 'Mean estimated relaxation time'
    )
        
    
    ax.set_xlabel("Estimated relaxation time (s)")
    ax.set_ylabel("Number of realizations")
    ax.set_title("Monte Carlo Estimation of Brownian Relaxation Time")
    ax.legend()

    fig.tight_layout()
    fig.savefig(
    "monte_carlo_histogram.png",
    dpi=300,
    bbox_inches="tight"
)
    plt.show()
    
    

    
    
def  plot_particle_motion(t, c_true, m_true, m_measured, m_fitted):
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    ax.plot(t, c_true, color="blue", label="Trap center")
    ax.plot(t, m_true, color="green", label="True mean position")

    ax.plot(
    t, m_fitted,
    color="red",
    linestyle="--",
    label="Fitted mean position"
    )

    ax.scatter(
    t, m_measured,
    color="orange",
    s=18,
    alpha=0.6,
    label="Noisy measurements"
    )  
    
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Position (µm)")
    ax.set_title("Brownian Particle in an Oscillating Optical Trap")

    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()

    fig.savefig(
    "particle_motion.png",
    dpi=300,
    bbox_inches="tight"
    )

    plt.show()

  
    
      
      
      
      
      
      
      
        