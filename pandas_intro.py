import pandas as pd

# Data dictionary
data = {
    'rocket': ['Falcon 1', 'Falcon 9', 'Falcon Heavy'],
    'launches': [5, 100, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the entire DataFrame
print("DataFrame:")
print(df)

# Print the 'rocket' column
print("\nRocket Column:")
print(df['rocket'])

# Filter for rockets with more than 5 launches
filtered_df = df[df['launches'] > 5]
print("\nRockets with more than 5 launches:")
print(filtered_df)

# Add the 'success_rate' column
df['success_rate'] = [0.4, 0.98, 1.0]

# Print the updated DataFrame with success rate
print("\nDataFrame with Success Rate:")
print(df)
