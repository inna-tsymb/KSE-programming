import matplotlib.pyplot as plt

# Data for the charts
categories = ["Yes", "No"]
colors = ["#56B4E9", "#E69F00"]

# Data values and confidence intervals
data = {
    "Overall": {"values": [35.5, 66.5], "ci": [(18.6, 52.3), (47.7, 81.4)]},
    "Type of Exposure": {"values": [99.4, 0.6], "ci": [(98.1, 100), (0.1, 1.9)]},
    "Females": {"values": [51.0, 49.0], "ci": [(24.2, 77.8), (22.2, 75.8)]},
    "Males": {"values": [28.0, 72.0], "ci": [(13.5, 42.4), (57.6, 86.5)]}
}

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.flatten()

# Plot each chart
for i, (title, content) in enumerate(data.items()):
    values = content["values"]
    ci = content["ci"]
    bars = axs[i].bar(categories, values, yerr=[[v - c[0] for v, c in zip(values, ci)],
                                                [c[1] - v for v, c in zip(values, ci)]],
                      capsize=10, color=colors)
    axs[i].set_title(title, fontsize=50)
    axs[i].set_ylabel("Proportion (%)", fontsize=20)
    axs[i].tick_params(axis='x', labelsize=35)
    axs[i].tick_params(axis='y', labelsize=35)

plt.tight_layout()
#plt.savefig("arv_exposure_bar_charts.png")
plt.show()