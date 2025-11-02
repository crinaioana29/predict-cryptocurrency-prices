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
filtered_df = df[df['crypto_name'].isin(['Bitcoin', 'Litecoin'])]
print("filtered_df shape: ", filtered_df.shape)
print("Unique cryptocurrencies in filtered_df: ", filtered_df['crypto_name'].unique())
print("\n")
