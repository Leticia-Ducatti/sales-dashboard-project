# Projeto: streamlit-sales-insights
# Este projeto é um dashboard interativo para análise de dados de vendas.
# Construído com Python e Streamlit, permite filtragem por categoria e mês,
# exibe métricas principais (vendas totais, número de pedidos, ticket médio),
# sendo ideal para demonstrar habilidades em análise de dados e desenvolvimento de aplicações web.

import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

# Carregando os dados
@st.cache_data
def load_data():
    df = pd.read_csv("Sales_Data_Project1.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Weekday"] = df["Order Date"].dt.day_name()
    df["Month"] = df["Order Date"].dt.strftime('%Y-%m')
    return df

df = load_data()

# Filtros interativos
st.sidebar.header("Filtros")
categorias = st.sidebar.multiselect(
    "Categoria do Produto:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

meses = st.sidebar.multiselect(
    "Mês:",
    options=sorted(df["Month"].unique()),
    default=sorted(df["Month"].unique())
)

df = df[
    (df["Category"].isin(categorias)) &
    (df["Month"].isin(meses))
]

# Exibição dos dados
st.subheader("🔍 Preview do Dataset")
st.dataframe(df.head())

# Métricas principais
total_sales = df["Sales"].sum()
total_orders = df.shape[0]
avg_ticket = total_sales / df["Quantity"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("🧾 Total Orders", total_orders)
col3.metric("🎟️ Avg. Ticket", f"${avg_ticket:,.2f}")
