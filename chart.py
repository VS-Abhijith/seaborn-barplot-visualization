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

# Barplot (clean, no title)
sns.barplot(data=df, x="Product", y="Sales", hue="Product", legend=False, palette="viridis")

# Axis labels (optional — remove if you want totally clean)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Sales (Units)", fontsize=12)

# Save chart (no extra borders, exactly 512x512)
plt.savefig("chart.png", dpi=100, bbox_inches=None, pad_inches=0)
plt.close()
