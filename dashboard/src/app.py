import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Configurações do banco de dados
DATABASE_HOST = os.getenv('POSTGRES_HOST')
DATABASE_USER = os.getenv('POSTGRES_USER')
DATABASE_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DATABASE_DB = os.getenv('POSTGRES_DB')

# String de conexão com o PostgreSQL
connection_string = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}'

# Criando o engine do SQLAlchemy
engine = create_engine(connection_string)

# Função para ler os dados usando SQLAlchemy e Pandas
def read_data(sql_query):
    with engine.connect() as conn:
        data = pd.read_sql(sql_query, conn)
    return data

# Exemplo de consulta SQL para carregar dados de vendas
sql_query_sales = """
SELECT s.id, u.name AS user_name, p.name AS product_name, s.quantity, s.sale_price
FROM public.sales AS s
JOIN public.users AS u ON s.customer_id = u.id
JOIN public.products AS p ON s.product_id = p.id;
"""

# Carregar os dados
sales_data = read_data(sql_query_sales)

# Criar o dashboard
st.title('Dashboard de Vendas')

# Exibir os dados de vendas como tabela
st.header('Dados de Vendas')
st.dataframe(sales_data)

# KPIs Exemplo
total_sales = sales_data['sale_price'].sum()
total_products = len(sales_data['product_name'].unique())
total_customers = len(sales_data['user_name'].unique())

# Exibir KPIs
st.metric(label="Vendas Totais", value=f"R$ {total_sales}")
st.metric(label="Total de Produtos Vendidos", value=total_products)
st.metric(label="Total de Clientes", value=total_customers)

# Você pode adicionar mais KPIs e visualizações conforme necessário.
