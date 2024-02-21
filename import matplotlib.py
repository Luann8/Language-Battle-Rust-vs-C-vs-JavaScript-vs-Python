import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo - pontuações atribuídas a cada linguagem em diferentes critérios
dados = {
    'Linguagem': ['Python', 'C', 'Rust', 'JavaScript'],
    'Desempenho': [8, 9, 9, 6],
    'Segurança': [7, 8, 9, 5],
    'Facilidade de Uso': [8, 6, 7, 7],
    'Comunidade': [9, 7, 8, 6],
    'Velocidade': [6, 9, 9, 7]  # Adicionando a pontuação de velocidade
}

# Criar DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Calcular a pontuação total para cada linguagem
df['Pontuação Total'] = df.drop('Linguagem', axis=1).sum(axis=1)

# Ordenar o DataFrame pela pontuação total
df = df.sort_values(by='Pontuação Total', ascending=False)

# Plotar o gráfico de barras
plt.figure(figsize=(10, 6))
bar_plot = plt.bar(df['Linguagem'], df['Pontuação Total'], color=['blue', 'green', 'orange', 'red'])

# Adicionar valores no topo das barras e informações de pontuação para cada critério
for i, bar in enumerate(bar_plot):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    plt.text(bar.get_x() + bar.get_width()/2, -3.5, f"Desempenho: {df['Desempenho'].iloc[i]}\nSegurança: {df['Segurança'].iloc[i]}\nFacilidade de Uso: {df['Facilidade de Uso'].iloc[i]}\nComunidade: {df['Comunidade'].iloc[i]}\nVelocidade: {df['Velocidade'].iloc[i]}", ha='center', va='top')

plt.xlabel('')
plt.ylabel('Pontuação Total')
plt.title('Comparação de Linguagens de Programação')
plt.ylim(0, 45)  # Definir o limite do eixo y
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=0)  # Rotacionar os rótulos do eixo x para facilitar a leitura
plt.tight_layout()  # Ajustar layout para que todas as informações sejam visíveis
plt.show()
