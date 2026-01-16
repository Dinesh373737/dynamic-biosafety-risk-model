import matplotlib
matplotlib.use("Agg")
import math
import matplotlib.pyplot as plt                               
# R0 values (independent variable)
R0_values = [
    0.8, 1.0, 1.2, 1.4, 1.6,
    1.8, 2.0, 2.3, 2.6, 3.0, 3.5
]

# Normalization
R0_max = 5.0
R0_normalized = [math.log(r) / math.log(R0_max) for r in R0_values]

# Fixed contribution from other parameters
# (CFR, mutation rate, transmission, etc.)
background_risk = 0.35

# Final risk score calculation
risk_scores = [
    100 * (0.5 * r_norm + 0.5 * background_risk)
    for r_norm in R0_normalized
]

# Plotting
plt.figure()
plt.plot(R0_values, risk_scores, marker='o')
plt.xlabel("Basic Reproduction Number (R₀)")
plt.ylabel("Risk Score (0–100)")
plt.title("Effect of Pathogen Transmissibility (R₀) on Biosafety Risk Score")
plt.grid(True)
plt.savefig("risk_vs_r0.png", dpi=300, bbox_inches="tight")
plt.axhline(30, linestyle='--', linewidth=1)
plt.axhline(55, linestyle='--', linewidth=1)
plt.axhline(80, linestyle='--', linewidth=1)

print("Graph saved as risk_vs_r0.png")

