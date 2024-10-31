import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_excel("Mobile_Purchases_2019_2024.xlsx")

# Convert Purchase_Date to datetime and extract Year for Year-wise Analysis
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
df['Year'] = df['Purchase_Date'].dt.year

# Set Seaborn style for modern visuals
sns.set(style="whitegrid")

# Slide 1: Market Share by Brand
plt.figure(figsize=(8, 6))
brand_counts = df['Brand'].value_counts(normalize=True) * 100
sns.barplot(x=brand_counts.index, y=brand_counts.values, palette="viridis")
plt.title('Market Share by Brand (%)', fontsize=16, fontweight='bold')
plt.xlabel("Brand", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=14)

# Add percentage annotations on bars
for i, value in enumerate(brand_counts.values):
    plt.text(i, value + 1, f"{value:.1f}%", ha='center', fontsize=12)
plt.show()

# Slide 2: Yearly Sales Trend by Brand
plt.figure(figsize=(10, 6))
yearly_sales = df.groupby(['Year', 'Brand']).size().unstack()
yearly_sales.plot(kind='line', marker='o', colormap="viridis", linewidth=2.5)
plt.title('Yearly Sales Trend by Brand', fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.legend(title="Brand")
plt.show()

# Slide 3: Price Distribution by Brand
plt.figure(figsize=(10, 6))
sns.boxplot(x="Brand", y="Price", data=df, palette="Set3")
plt.title('Price Distribution by Brand', fontsize=16, fontweight='bold')
plt.xlabel("Brand", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.show()

# Slide 4: Popular Brand by State
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='State', order=df['State'].value_counts().index, hue='Brand', palette="pastel")
plt.title('Popular Brand by State', fontsize=16, fontweight='bold')
plt.xlabel("State", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(rotation=45)
plt.legend(title="Brand")
plt.show()

# Combined Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Mobile Market Analysis Dashboard (2019 - 2024)", fontsize=20, fontweight='bold', color='#333333')

# Market Share by Brand
sns.barplot(x=brand_counts.index, y=brand_counts.values, ax=axes[0, 0], palette="viridis")
axes[0, 0].set_title('Market Share by Brand (%)', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel("Brand", fontsize=12)
axes[0, 0].set_ylabel("Percentage (%)", fontsize=12)

# Yearly Sales Trend by Brand
yearly_sales.plot(kind='line', marker='o', ax=axes[0, 1], colormap="viridis", linewidth=2)
axes[0, 1].set_title('Yearly Sales Trend by Brand', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel("Year", fontsize=12)
axes[0, 1].set_ylabel("Number of Sales", fontsize=12)

# Price Distribution by Brand
sns.boxplot(x="Brand", y="Price", data=df, ax=axes[1, 0], palette="Set3")
axes[1, 0].set_title('Price Distribution by Brand', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel("Brand", fontsize=12)
axes[1, 0].set_ylabel("Price", fontsize=12)

# Popular Brand by State
sns.countplot(data=df, x='State', order=df['State'].value_counts().index, hue='Brand', ax=axes[1, 1], palette="pastel")
axes[1, 1].set_title('Popular Brand by State', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel("State", fontsize=12)
axes[1, 1].set_ylabel("Count", fontsize=12)
axes[1, 1].tick_params(axis='x', rotation=45)

# Final adjustments for spacing
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
