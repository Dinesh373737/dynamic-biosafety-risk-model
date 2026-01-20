import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# Mutation rate values (normalized)
mutation_rates = [0.05, 0.10, 0.20, 0.35, 0.50]

# Corresponding BSL levels (scenario-based)
bsl_levels = [2.0, 2.5, 3.0, 3.5, 4.0]

# Plot
plt.figure()
plt.plot(mutation_rates, bsl_levels, marker='o')

plt.xlabel("Mutation Rate")
plt.ylabel("Recommended Biosafety Level (BSL)")
plt.title("Impact of Mutation Rate on Biosafety Level Escalation")
plt.grid(True)

# Optional: clearer y-axis
plt.yticks([2, 2.5, 3, 3.5, 4])

# Save
plt.savefig("mutation_rate_vs_bsl.png", dpi=300, bbox_inches="tight")
print("Graph saved as mutation_rate_vs_bsl.png")
