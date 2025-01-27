import pandas as pd

# Create a table (DataFrame) of data
data = {'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300]}
df = pd.DataFrame(data)

# Calculate total sales
total_sales = df['Sales'].sum()
print(total_sales)  # Output: 600
