import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [120, 95, 140, 80, 110]
}
df = pd.DataFrame(data)

# Create figure with exact size (512x512 at dpi=100 → 5.12 inches)
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Barplot (with hue set to avoid warning)
sns.barplot(data=df, x="Product", y="Sales", hue="Product", legend=False, palette="viridis")

# Titles and labels
plt.title("Quarterly Sales Performance by Product", fontsize=16, pad=15)
plt.xlabel("Product", fontsize=14)
plt.ylabel("Sales (Units)", fontsize=14)

# Save chart in repo folder
plt.savefig("chart.png", dpi=100, bbox_inches="tight")
plt.close()
