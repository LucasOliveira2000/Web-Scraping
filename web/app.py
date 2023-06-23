import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Placas de Vídeo Kabum")

# Exibição dos dados
st.title("Relatorio do Web Scraping - KABUM:shopping_trolley:")

# Opções de seleção
opcao = st.sidebar.radio(
    "Selecione uma opção",
    ["Valor a Vista", "Valor a Vista e Valor no Cartão", "Esgotados"]
)

if opcao == "Valor a Vista":
    # Exibição dos dados de placas de vídeo a vista
    st.header("Placas de Vídeo a Vista")
    dados = pd.read_excel("valor_a_vista.xlsx")  # Lê o arquivo "valor_a_vista.xlsx" e armazena os dados em um DataFrame chamado "dados"
    coluna_selecionada = 'Valor do Produto'  # Define a coluna selecionada como 'Valor do Produto'
    st.dataframe(dados[['Nome do Produto', 'Valor do Produto']])  # Exibe os dados selecionados do DataFrame em uma tabela
    



if opcao == "Valor a Vista e Valor no Cartão":
    # Exibição dos dados de placas de vídeo a vista e no cartão
    st.header("Placas de Vídeo a Vista e no Cartão")
    dados_a_vista = pd.read_excel("valor_a_vista.xlsx")  # Lê o arquivo "valor_a_vista.xlsx" e armazena os dados em um DataFrame chamado "dados_a_vista"
    dados_cartao = pd.read_excel("valor_no_cartao.xlsx")  # Lê o arquivo "valor_no_cartao.xlsx" e armazena os dados em um DataFrame chamado "dados_cartao"
    dados_combinados = pd.merge(dados_a_vista, dados_cartao, on='Nome do Produto', how='inner')  # Combina os dados dos dois DataFrames usando a coluna 'Nome do Produto'
    st.dataframe(dados_combinados[['Nome do Produto', 'Valor do Produto', 'Valor no Cartão']])  # Exibe os dados selecionados do DataFrame combinado em uma tabela

elif opcao == "Esgotados":
    # Exibição dos produtos esgotados
    st.header("Placas de Vídeo Esgotadas")
    dados_esgotados = pd.read_excel("sem_estoque.xlsx")  # Lê o arquivo "sem_estoque.xlsx" e armazena os dados em um DataFrame chamado "dados_esgotados"
    coluna_selecionada = 'Produtos'  # Define a coluna selecionada como 'Produtos'
    st.dataframe(dados_esgotados,height=900, width=1000)  # Exibe todos os dados do DataFrame em uma tabela




   