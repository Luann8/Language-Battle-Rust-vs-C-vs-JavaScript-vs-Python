import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Language': ['Python', 'C', 'Rust', 'JavaScript'],
    'Performance': [8, 9, 9, 6],
    'Security': [7, 8, 9, 5],
    'Ease of Use': [8, 6, 7, 7],
    'Community': [9, 7, 8, 6],
    'Speed': [6, 9, 9, 7]  
}

df = pd.DataFrame(data)

df['Total Score'] = df.drop('Language', axis=1).sum(axis=1)

df = df.sort_values(by='Total Score', ascending=False)

plt.figure(figsize=(10, 6))
bar_plot = plt.bar(df['Language'], df['Total Score'], color=['blue', 'green', 'orange', 'red'])

for i, bar in enumerate(bar_plot):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width()/2, -3.5, f"Performance: {df['Performance'].iloc[i]}\nSecurity: {df['Security'].iloc[i]}\nEase of Use: {df['Ease of Use'].iloc[i]}\nCommunity: {df['Community'].iloc[i]}\nSpeed: {df['Speed'].iloc[i]}", ha='center', va='top')

plt.xlabel('')
plt.ylabel('Total Score')
plt.title('Programming Languages Comparison')
plt.ylim(0, 45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
