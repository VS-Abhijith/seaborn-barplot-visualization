import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate synthetic business data
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [120, 150, 90, 200, 170]
}
df = pd.DataFrame(data)

# Set seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create a figure with exact size for 512x512 pixels at dpi=100
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Create barplot
sns.barplot(data=df, x="Product", y="Sales", palette="viridis")

# Add titles and labels
plt.title("Product Sales Performance", fontsize=16)
plt.xlabel("Product")
plt.ylabel("Sales Units")

# Save chart as 512x512 PNG
output_path = "/mnt/data/chart.png"
plt.savefig(output_path, dpi=100, bbox_inches="tight")

plt.close()

output_path
