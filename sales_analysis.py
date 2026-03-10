import pandas as pd
import matplotlib.pyplot as plt
import os

# ================================
# STEP 1: Load Dataset
# ================================
df = pd.read_csv("data/sales.csv")

# ================================
# STEP 2: Data Cleaning
# ================================
df['Date'] = pd.to_datetime(df['Date'])  # convert date format
df['Total'] = df['Price'] * df['Quantity']  # revenue column

print("\nCLEANED DATA:\n")
print(df)

# ================================
# STEP 3: Key Insights
# ================================
print("\n==============================")
print("🔹 Total Revenue:")
print(df['Total'].sum())

print("\n==============================")
print("🔹 Top Selling Products:")
print(df.groupby('Product')['Total'].sum().sort_values(ascending=False))

print("\n==============================")
print("🔹 Category Performance:")
print(df.groupby('Category')['Total'].sum())

# ================================
# STEP 4: Monthly Revenue Trend
# ================================
monthly_rev = df.groupby(df['Date'].dt.month)['Total'].sum()

plt.figure(figsize=(8,4))
plt.plot(monthly_rev.index, monthly_rev.values, marker='o', linewidth=2)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

# Save Chart
chart_path = "charts/monthly_revenue.png"

# Create chart folder if not exists
os.makedirs("charts", exist_ok=True)
plt.savefig(chart_path)

print("\nChart saved at:", chart_path)
plt.show()

# ================================
# STEP 5: Export Cleaned Data
# ================================
df.to_csv("data/cleaned_sales.csv", index=False)
print("\nCleaned file saved: data/cleaned_sales.csv")