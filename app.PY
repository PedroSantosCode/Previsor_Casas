import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

# =====================
# 1. Base de dados (exemplo simples)
# =====================
# metros quadrados e preços em mil reais
dados = {
    'area': [50, 60, 80, 100, 120, 150],
    'preco': [200, 240, 320, 400, 480, 600]
}

df = pd.DataFrame(dados)

# =====================
# 2. Treinar o modelo
# =====================
X = df[['area']]
y = df[['preco']]
modelo = LinearRegression()
modelo.fit(X, y)

# =====================
# 3. Interface Streamlit
# =====================
st.title("🏠 Previsor de Preço de Casas")
st.write("Digite a área do imóvel em metros quadrados:")

area = st.number_input("Área (m²)", min_value=10, max_value=1000, step=5)

if area:
    preco_previsto = modelo.predict([[area]])[0][0]
    st.success(f"O preço estimado da casa é de R$ {preco_previsto:,.2f} mil")
