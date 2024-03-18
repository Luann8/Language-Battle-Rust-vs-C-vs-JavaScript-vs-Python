import matplotlib.pyplot as plt
import pandas as pd

# Existing data
data = {
    'Language': ['Python', 'C', 'Rust', 'JavaScript'],
    'Performance': [8, 9, 9, 6],
    'Security': [7, 8, 9, 5],
    'Ease of Use': [8, 6, 7, 7],
    'Community': [9, 7, 8, 6],
    'Speed': [6, 9, 9, 7]  
}

# New 'Golang' row
golang_data = {
    'Language': ['Golang'],
    'Performance': [9],
    'Security': [8],
    'Ease of Use': [8],
    'Community': [7],
    'Speed': [9]  
}

# Concatenate data to DataFrame
data = pd.concat([pd.DataFrame(data), pd.DataFrame(golang_data)], ignore_index=True)

# Calculate Total Score
data['Total Score'] = data.drop('Language', axis=1).sum(axis=1)

# Sort DataFrame by Total Score
data = data.sort_values(by='Total Score', ascending=False)

# Assign colors to each language
colors = {
    'Python': 'blue',
    'C': 'green',
    'Rust': 'orange',
    'JavaScript': 'red',
    'Golang': 'yellow'
}

# Plot
plt.figure(figsize=(10, 6))
bar_plot = plt.bar(data['Language'], data['Total Score'], color=[colors[lang] for lang in data['Language']])

for i, bar in enumerate(bar_plot):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width()/2, -3.5, f"Performance: {data['Performance'].iloc[i]}\nSecurity: {data['Security'].iloc[i]}\nEase of Use: {data['Ease of Use'].iloc[i]}\nCommunity: {data['Community'].iloc[i]}\nSpeed: {data['Speed'].iloc[i]}", ha='center', va='top')

plt.xlabel('')
plt.ylabel('Total Score')
plt.title('Programming Languages Comparison')
plt.ylim(0, 45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
