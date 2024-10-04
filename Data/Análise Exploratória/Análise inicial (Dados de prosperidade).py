
# Bibliotecas usadas na análise:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados do arquivo CSV
dados = pd.read_csv('data.csv')

# Métodos para explorar os dados
# Exibe as primeiras linhas do arquivo
print(dados.head())

# Exibe informações gerais sobre o dataset (tipos de dados e valores ausentes)
dados.info()

# Exibe contagem de valores não nulos, média, desvio padrão, valor mínimo, quartis e valor máximo
dados.describe()

# Verifica valores nulos
dados.isnull().sum()
(dados.isnull().sum() / len(dados)) * 100

# Gráfico de Barras para análise comparativa
top_15 = dados[['Country', 'SafetySecurity']].sort_values(by='SafetySecurity', ascending=False).head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x='SafetySecurity', y='Country', data=top_15, palette='viridis')
plt.title('Top 15 Países por Pontuação de Segurança', fontsize=16)
plt.xlabel('Segurança', fontsize=12)
plt.ylabel('País', fontsize=12)
plt.tight_layout()
plt.show()

# Histograma para analisar distribuição de variáveis numéricas
plt.figure(figsize=(10, 6))
sns.histplot(dados['AveragScore'], bins=20, kde=True)
plt.title('Distribuição da Pontuação Média dos Países')
plt.xlabel('Pontuação Média')
plt.ylabel('Frequência')
plt.show()

