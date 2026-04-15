#Raw Data → EDA → Understanding → Visualization → Insights
import pandas as pd

df = pd.read_csv("hockey.csv")
# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Quick statistics summary
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print(df.duplicated().sum())

# Question 1: Which team won the most games in a single season?
best_team = df[df['Wins'] == df['Wins'].max()]
print("Best season ever:")
print(best_team)

# Question 2: Which team lost the most?
worst_team = df[df['Losses'] == df['Losses'].max()]
print("Worst season ever:")
print(worst_team)

# Question 3: Average wins per year — did teams improve over time?
avg_per_year = df.groupby('Year')['Wins'].mean()
print(avg_per_year)

# Check if 2004 is missing
print(df['Year'].unique())

# Count games per year
print(df.groupby('Year')['Team Name'].count())

# Which team won the most across ALL years?
total_wins = df.groupby('Team Name')['Wins'].sum()
total_wins_sorted = total_wins.sort_values(ascending=False)
print(total_wins_sorted.head(10))

# Calculate win percentage
df['Win%'] = df['Wins'] / (df['Wins'] + df['Losses']) * 100
df['Win%'] = df['Win%'].round(2)
print(df.head())

# Best win percentage ever
best_winpct = df[df['Win%'] == df['Win%'].max()]
print("Best Win% ever:")
print(best_winpct)

# Worst win percentage ever
worst_winpct = df[df['Win%'] == df['Win%'].min()]
print("Worst Win% ever:")
print(worst_winpct)

# Average win percentage per team across all years
avg_winpct = df.groupby('Team Name')['Win%'].mean().round(2)
avg_winpct_sorted = avg_winpct.sort_values(ascending=False)
print("Top 10 teams by average Win%:")
print(avg_winpct_sorted.head(10))

# Do wins and losses correlate negatively?
correlation = df[['Wins', 'Losses', 'Win%']].corr()
print(correlation)