# Normalização
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

dados[['SafetySecurity', 'PersonelFreedom', 'Governance']] = scaler.fit_transform(
    dados[['SafetySecurity', 'PersonelFreedom', 'Governance']])


# Codificação da coluna "Country"
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

dados['Country_encoded'] = label_encoder.fit_transform(dados['Country'])

print(dados[['Country', 'Country_encoded']].head())


# Divisão de Dados
from sklearn.model_selection import train_test_split

X = dados.drop(columns=['AveragScore'])  
y = dados['AveragScore']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Treinamento
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

modelo_regressao = LinearRegression()

modelo_regressao.fit(X_train, y_train)

y_pred = modelo_regressao.predict(X_test)

mse = mean_squared_error(y_test, y_pred)  # Erro quadrático médio
r2 = r2_score(y_test, y_pred)  # R-quadrado (coeficiente de determinação)

print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"Coeficiente de Determinação (R²): {r2:.2f}")

print("Coeficientes da Regressão Linear:", modelo_regressao.coef_)
print("Intercepto da Regressão Linear:", modelo_regressao.intercept_)


# Gráfico de dispersão com a linha de regressão
plt.figure(figsize=(10, 6))

plt.scatter(y_test, y_pred, color='blue', edgecolor='k', alpha=0.6)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)

plt.title("Regressão Linear: Valores Reais vs. Valores Previstos", fontsize=16)
plt.xlabel("Valores Reais (y_test)", fontsize=14)
plt.ylabel("Valores Previstos (y_pred)", fontsize=14)

plt.show()




