import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import math

# Outbreak stages
stages = ["Emerging", "Peak", "Controlled"]
multipliers = [1.25, 1.15, 0.85]

# Fixed R0 and background risk
R0 = 2.0
R0_max = 5.0
R0_norm = math.log(R0) / math.log(R0_max)

background_risk = 0.35

# Base risk score
base_risk = 100 * (0.5 * R0_norm + 0.5 * background_risk)

# Final risk scores per stage
risk_scores = [base_risk * m for m in multipliers]

# Plot (bar chart is best here)
plt.figure()
plt.bar(stages, risk_scores)
plt.xlabel("Outbreak Stage")
plt.ylabel("Risk Score (0–100)")
plt.title("Effect of Outbreak Stage on Biosafety Risk Score")
plt.grid(axis="y")
plt.axhline(30, linestyle='--', linewidth=1)
plt.axhline(55, linestyle='--', linewidth=1)
plt.axhline(80, linestyle='--', linewidth=1)

# Save figure
plt.savefig("risk_vs_outbreak_stage.png", dpi=300, bbox_inches="tight")
print("Graph saved as risk_vs_outbreak_stage.png")
