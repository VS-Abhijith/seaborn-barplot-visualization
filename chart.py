# chart.py
# Author: Abhijith
# Email: 22ds3000188@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ----------------------------
# 1. Generate realistic synthetic data
# ----------------------------
# Business context: Product performance across categories (Sales Revenue in $K)
data = {
    "Product": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
    "Sales": [120, 90, 150, 80, 110]  # synthetic business data in $K
}
df = pd.DataFrame(data)

# ----------------------------
# 2. Apply professional styling
# ----------------------------
sns.set_style("whitegrid")                # clean background
sns.set_context("talk")                   # presentation-ready labels
palette = sns.color_palette("viridis", 5) # professional color palette

# ----------------------------
# 3. Create barplot
# ----------------------------
plt.figure(figsize=(8, 8))  # ensures ~512x512 pixels at dpi=64
sns.barplot(x="Product", y="Sales", data=df, palette=palette)

# ----------------------------
# 4. Customize plot
# ----------------------------
plt.title("Quarterly Sales Performance by Product", fontsize=18, weight="bold")
plt.xlabel("Product", fontsize=14)
plt.ylabel("Sales Revenue ($K)", fontsize=14)

# ----------------------------
# 5. Export PNG (exactly 512x512 pixels)
# ----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
