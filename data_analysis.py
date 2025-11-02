import pandas as pd
import numpy as p
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset csv
df = pd.read_csv('dataset.csv')
print(df.head())
print("\n")

# Print shape of the dataset
print("dataset.csv shape: ", df.shape)
print("\n")

# Display unique cryptocurrencies
print("Unique cryptocurrencies: ", df['crypto_name'].unique())
print("\n")

# Filter dataset for Bitcoin and Litecoin
filtered_df = df[df['crypto_name'].isin(['Bitcoin', 'Litecoin'])].copy()
print("filtered_df shape: ", filtered_df.shape)
print("Unique cryptocurrencies in filtered_df: ", filtered_df['crypto_name'].unique())
print("\n")

# Calculate daily returns for each crypto
filtered_df['daily_return'] = filtered_df.groupby('crypto_name')['close'].pct_change()*100

# Calculate rolling averages of closing prices
filtered_df['moving_avg_20'] = filtered_df.groupby('crypto_name')['close'].transform(lambda x: x.rolling(20).mean())
filtered_df['moving_avg_50'] = filtered_df.groupby('crypto_name')['close'].transform(lambda x: x.rolling(50).mean())

# Calculate rolling volatility (standard deviation of returns)
filtered_df['volatility'] = filtered_df.groupby('crypto_name')['daily_return'].transform(lambda x: x.rolling(20).std())

print("filtered_df after adding daily returns, moving_avg_20, moving_avg_50 and volatility columns: ")
print(filtered_df.head())
print("\n")

