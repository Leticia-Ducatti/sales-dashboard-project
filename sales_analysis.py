import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset CSV
df = pd.read_csv("sales_data_project1.csv")  

# Ver as primeiras linhas
print("🔍 Preview do dataset:")
print(df.head())

# Informações gerais
print("\n📋 Informações do dataset:")
print(df.info())

# Estatísticas descritivas
print("\n📊 Estatísticas:")
print(df.describe())

# Verificar valores nulos
print("\n❌ Valores nulos por coluna:")
print(df.isnull().sum())

# Remover duplicatas se existirem
df = df.drop_duplicates()

# Converter coluna de data
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Criar colunas de tempo úteis
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Weekday"] = df["Order Date"].dt.day_name()

# 📈 Gráficos

# Vendas por categoria
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum)
plt.title("Total Sales by Category")
plt.show()

# Vendas por região
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Region", y="Sales", estimator=sum)
plt.title("Total Sales by Region")
plt.show()

# Tendência de vendas mensais
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x="Month", y="Sales", marker="o")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
print("📸 Gráfico salvo como 'monthly_sales_trend.png'")
plt.show()

# 📦 Análises adicionais

# 1. Top produtos mais vendidos (por quantidade)
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Produtos Mais Vendidos (por Quantidade)")
plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")
plt.tight_layout()
plt.show()

# 2. Região com maior faturamento
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Faturamento Total por Região")
plt.ylabel("Total de Vendas")
plt.xlabel("Região")
plt.tight_layout()
plt.show()

# 3. Vendas por dia da semana
weekday_sales = df.groupby("Weekday")["Sales"].sum()
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_sales = weekday_sales.reindex(weekday_order)
plt.figure(figsize=(10, 5))
sns.barplot(x=weekday_sales.index, y=weekday_sales.values, palette="magma")
plt.title("Total de Vendas por Dia da Semana")
plt.ylabel("Total de Vendas")
plt.xlabel("Dia da Semana")
plt.tight_layout()
plt.show()

# 4. Ticket médio por venda
df["Ticket Médio"] = df["Sales"] / df["Quantity"]
plt.figure(figsize=(8, 5))
sns.histplot(df["Ticket Médio"], bins=20, kde=True, color="skyblue")
plt.title("Distribuição do Ticket Médio por Venda")
plt.xlabel("Ticket Médio")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

# 5. Top clientes por volume de compras
top_customers = df.groupby("Customer ID")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="plasma")
plt.title("Top 10 Clientes por Volume de Compras")
plt.xlabel("Total em Vendas")
plt.ylabel("Cliente")
plt.tight_layout()
plt.show()