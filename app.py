import streamlit as st
from faker import Faker
import pandas as pd
import random

# Inicializa o Faker
fake = Faker()

# Função para gerar dados fictícios de vendas
def gerar_dados_vendas(n, tipo):
    dados = []
    for _ in range(n):
        dados.append({
            'Produto': fake.word(),
            'Vendas': random.randint(1000, 10000) if tipo == 'B2B' else random.randint(500, 5000),
            'Estoque Atual': random.randint(500, 5000) if tipo == 'B2B' else random.randint(100, 2000),
            'Estoque Desejado': random.randint(1000, 8000) if tipo == 'B2B' else random.randint(500, 3000),
            'Tipo': tipo
        })
    return pd.DataFrame(dados)

# Função para calcular OTB
def calcular_otb(df):
    df['OTB'] = (df['Vendas'] + df['Estoque Desejado']) - df['Estoque Atual']
    return df

# Configuração do Streamlit
st.title("OTB (Open-to-Buy)")
st.subheader("Dashboard OTB  - B2B & B2C")

# Entrada de usuário
num_produtos_b2c = st.sidebar.slider("Número de Produtos B2C", 5, 50, 10)
num_produtos_b2b = st.sidebar.slider("Número de Produtos B2B", 5, 50, 10)

df_b2c = gerar_dados_vendas(num_produtos_b2c, 'B2C')
df_b2b = gerar_dados_vendas(num_produtos_b2b, 'B2B')

df_otb = calcular_otb(pd.concat([df_b2c, df_b2b]))

# Exibe os dados
st.subheader("📊 Dados de Vendas e OTB")
st.dataframe(df_otb)

# Métricas totais
st.subheader("📈 Resumo Geral")

for tipo in ['B2C', 'B2B']:
    df_tipo = df_otb[df_otb['Tipo'] == tipo]

    vendas_totais = df_tipo['Vendas'].sum()
    estoque_atual_total = df_tipo['Estoque Atual'].sum()
    estoque_desejado_total = df_tipo['Estoque Desejado'].sum()
    otb_total = df_tipo['OTB'].sum()

    st.markdown(f"### {tipo}")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"<small>Vendas Totais</small><br><b>R$ {vendas_totais:,.2f}</b>", unsafe_allow_html=True)
    col2.markdown(f"<small>Estoque Atual</small><br><b>R$ {estoque_atual_total:,.2f}</b>", unsafe_allow_html=True)
    col3.markdown(f"<small>Estoque Desejado</small><br><b>R$ {estoque_desejado_total:,.2f}</b>", unsafe_allow_html=True)
    col4.markdown(f"<small>OTB Total</small><br><b>R$ {otb_total:,.2f}</b>", unsafe_allow_html=True)

# Gráfico
st.subheader("📉 OTB por Produto")

for tipo in ['B2C', 'B2B']:
    st.markdown(f"### {tipo}")
    st.bar_chart(df_otb[df_otb['Tipo'] == tipo].set_index('Produto')['OTB'])

st.write("🔍 Ajuste os parâmetros no menu lateral para simular diferentes cenários.")
