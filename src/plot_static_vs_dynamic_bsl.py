import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# Scenarios / stages
stages = ["Emerging", "Peak", "Controlled"]

# Static and dynamic BSL values
static_bsl = [2.5, 2.5, 2.5]
dynamic_bsl = [3.0, 3.5, 2.0]

# Plot
plt.figure()
plt.plot(stages, static_bsl, marker='o', label="Static BSL")
plt.plot(stages, dynamic_bsl, marker='o', label="Dynamic BSL")

plt.xlabel("Outbreak Stage")
plt.ylabel("Biosafety Level (BSL)")
plt.title("Comparison of Static and Dynamic Biosafety Level Recommendations")
plt.legend()
plt.grid(True)

# Save
plt.savefig("static_vs_dynamic_bsl.png", dpi=300, bbox_inches="tight")
print("Graph saved as static_vs_dynamic_bsl.png")
