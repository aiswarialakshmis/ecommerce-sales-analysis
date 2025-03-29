import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('ecommerce_sales.csv')

# Data Cleaning
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Total Revenue Calculation
total_revenue = df['Sales'].sum()
print(f'Total Revenue: ${total_revenue:,.2f}')

# Best-Selling Products
best_selling = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
print("Best-Selling Products:")
print(best_selling)

# Sales Trend Over Time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Order Date', y='Sales')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()