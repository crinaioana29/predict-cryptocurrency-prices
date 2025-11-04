import matplotlib
import pandas as pd
import numpy as p
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')

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
filtered_df['daily_return'] = filtered_df.groupby('crypto_name')['close'].pct_change() * 100

# Calculate rolling averages of closing prices
filtered_df['moving_avg_20'] = filtered_df.groupby('crypto_name')['close'].transform(lambda x: x.rolling(20).mean())
filtered_df['moving_avg_50'] = filtered_df.groupby('crypto_name')['close'].transform(lambda x: x.rolling(50).mean())

# Calculate rolling volatility (standard deviation of returns)
filtered_df['volatility'] = filtered_df.groupby('crypto_name')['daily_return'].transform(lambda x: x.rolling(20).std())

print("filtered_df after adding daily returns, moving_avg_20, moving_avg_50 and volatility columns: ")
print(filtered_df.head())
print("\n")

# Exploratory Data analysis
print("-----Exploratory Data Analysis-----")

# Filter dates and order them chronologically
filtered_df['date'] = pd.to_datetime(filtered_df['date'], format='%Y-%m-%d', errors='coerce')
filtered_df = filtered_df.sort_values('date').reset_index(drop=True)

# Plot closing price trends
for crypto in filtered_df['crypto_name'].unique():
    subset = filtered_df[filtered_df['crypto_name'] == crypto]
    plt.figure(figsize=(12, 6))
    plt.plot(subset['date'], subset['close'], label=crypto)
    plt.title(f'{crypto} Closing Prices Over Time (2013–2023)')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.savefig(f"{crypto}_closing_prices_2013_2023.png")
    plt.show(block=False)
plt.show()

# Histograms of closing prices for both cryptocurrencies
for crypto in filtered_df['crypto_name'].unique():
    plt.figure(figsize=(12, 6))
    sns.histplot(filtered_df[filtered_df['crypto_name'] == crypto]['close'], bins=80, kde=True)
    plt.title(f"Histogram of Closing Prices for {crypto}")
    plt.xlabel('Closing Price')
    plt.ylabel('Count')
    plt.savefig(f"{crypto}_closing_prices_histogram.png")
plt.show()

# Histograms of daily returns for both cryptocurrencies
for crypto in filtered_df['crypto_name'].unique():
    plt.figure(figsize=(12, 6))
    sns.histplot(filtered_df[filtered_df['crypto_name'] == crypto]['daily_return'] , bins=80, kde=True)
    plt.title(f"Histogram of Closing Prices for {crypto}")
    plt.xlabel('Daily Return (%)')
    plt.ylabel('Count')
    plt.savefig(f"{crypto}_daily_returns_histogram.png")
plt.show()

