# Gráfico de dispersão entre EconomicQuality e LivingConditions
plt.figure(figsize=(8, 6))
sns.scatterplot(data=dados, x='EconomicQuality', y='LivingConditions', hue='AverageScore', size='AverageScore', palette='cool', sizes=(20, 200))
plt.title('Relação Entre Qualidade Econômica e Condições de Vida', fontsize=14)
plt.xlabel('Qualidade Econômica', fontsize=12)
plt.ylabel('Condições de Vida', fontsize=12)
plt.legend(title='Índice de Prosperidade', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# Gráfico 2: Mapa de Correlação dos indicadores
import numpy as np

# Selecionando colunas numéricas
dados_numericos = dados[['SafetySecurity', 'PersonalFreedom', 'Governance', 
                         'SocialCapital', 'InvestmentEnvironment', 
                         'EnterpriseConditions', 'MarketAccessInfrastructure', 
                         'EconomicQuality', 'LivingConditions', 'Health', 
                         'Education', 'NaturalEnvironment']]

# Matriz de correlação
correlacoes = dados_numericos.corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlacoes, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True)
plt.title('Mapa de Correlação dos Indicadores', fontsize=14)
plt.tight_layout()
plt.show()