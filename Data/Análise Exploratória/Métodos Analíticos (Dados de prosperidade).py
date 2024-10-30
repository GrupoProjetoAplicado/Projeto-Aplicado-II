# Teste de Hipótese
from scipy import stats

media_hipotetica = 50

t_stat, p_val = stats.ttest_1samp(dados['AveragScore'], media_hipotetica)

print(f"Estatística t: {t_stat}")
print(f"Valor-p: {p_val}")

# Resultado
if p_val < 0.05:
    print("Rejeitamos a hipótese nula: a média difere significativamente de 50.")
else:
    print("Falhamos em rejeitar a hipótese nula: a média não difere significativamente de 50.")


# Análise de Variância
from scipy import stats

dados['Medias'] = dados[['SafetySecurity', 'PersonelFreedom', 'LivingConditions']].mean(axis=1)

dados['Grupo'] = pd.qcut(dados['Medias'], q=4, labels=['Baixo', 'Médio-baixo', 'Médio-alto', 'Alto'])


print(dados['Grupo'].value_counts())


grupos = [dados[dados['Grupo'] == grupo]['AveragScore'] for grupo in dados['Grupo'].unique()]

# Teste ANOVA
f_stat, p_val = stats.f_oneway(*grupos)

print(f"Estatística F: {f_stat}")
print(f"Valor-p: {p_val}")

# Resultado
if p_val < 0.05:
    print("Rejeitamos a hipótese nula: há diferença significativa entre as médias dos grupos.")
else:
    print("Falhamos em rejeitar a hipótese nula: não há diferença significativa entre as médias dos grupos.")