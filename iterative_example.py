import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Meu Dashboard Interativo")
st.write("Vamos ver como o Streamlit lida com dados e interações do usuário.")

###########################################################################################################################
###########################################################################################################################
# SEÇÃO 1: Captura de Dados (INPUTS)

st.header("1. Quem é você?")

# Criando duas colunas para organizar os campos de entrada lado a lado
col1, col2 = st.columns(2)

with col1:
    nome = st.text_input("Digite seu nome:", placeholder="Ex: Maria")

with col2:
    idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, value=20)

# O Streamlit processa e exibe o resultado imediatamente se o nome for preenchido
if nome:
    st.success(f"Olá, {nome}! Você tem {idade} anos e já está programando para a web! 🎉")

# FIM DA SEÇÃO 1: Captura de Dados (INPUTS)
###########################################################################################################################


###########################################################################################################################
###########################################################################################################################
# SEÇÃO 2: Gráficos e Dados

st.header("2. Visualização de Dados Simples")

# O usuário escolhe quantos pontos quer ver no gráfico através de um "Slider" (barra deslizante)
quantidade_pontos = st.slider("Escolha a quantidade de pontos para o gráfico:", min_value=10, max_value=100, value=50)

# Criando dados fictícios usando o Pandas e Numpy com base na escolha do usuário
dados_ficticios = pd.DataFrame(
    np.random.randn(quantidade_pontos, 2),
    columns=['Vendas Produto A', 'Vendas Produto B']
)

# Exibindo o gráfico de linhas (o Streamlit cria o gráfico com apenas uma linha de código!)
st.line_chart(dados_ficticios)

# Criando um botão para mostrar ou esconder a tabela com os dados brutos
if st.button("Ver dados brutos em formato de tabela"):
    st.write(dados_ficticios)

# FIM DA SEÇÃO 2: Gráficos e Dados
###########################################################################################################################


# https://docs.streamlit.io/get-started/fundamentals/main-concepts
# https://docs.streamlit.io/get-started/tutorials