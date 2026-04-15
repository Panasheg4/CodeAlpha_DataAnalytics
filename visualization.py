import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hockey.csv")

df['Win%'] = df['Wins'] / (df['Wins'] + df['Losses']) * 100
df['Win%'] = df['Win%'].round(2)

# Prepare the data
total_wins = df.groupby('Team Name')['Wins'].sum()
total_wins_sorted = total_wins.sort_values(ascending=False).head(10)

# Create the chart
plt.figure(figsize=(12, 6))
plt.barh(total_wins_sorted.index, total_wins_sorted.values, color='#8B0000')

# Labels and title
plt.title('Top 10 NHL Teams by Total Wins (1990-2011)', fontsize=16)
plt.xlabel('Team Name', fontsize=12)
plt.ylabel('Total Wins', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Show it
plt.tight_layout()
plt.show()


# Prepare data
avg_wins_year = df.groupby('Year')['Wins'].mean().round(2)

# Create chart
plt.figure(figsize=(12, 6))
plt.plot(avg_wins_year.index, avg_wins_year.values, 
         color='#8B0000', marker='x', linewidth=2)

# Labels
plt.title('Average NHL Wins Per Year (1990-2011)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Wins', fontsize=12)

# Highlight the lockout year
plt.axvline(x=2004, color='black', linestyle='--', label='2004 Lockout')
plt.legend()

plt.tight_layout()
plt.show()

# Prepare data
total_wins = df['Wins'].sum()
total_losses = df['Losses'].sum()

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    [total_wins, total_losses],
    labels=['Wins', 'Losses'],
    colors=['#8B0000', 'steelblue'],
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Overall NHL Win/Loss Distribution (1990-2011)', fontsize=16)
plt.show()


# Prepare data
corr = df[['Wins', 'Losses', 'Win%']].corr()

# Create heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    cmap='Reds',
    fmt='.2f',
    linewidths=0.5
)

plt.title('Correlation Heatmap', fontsize=16)
plt.tight_layout()
plt.show()