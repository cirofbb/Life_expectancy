import streamlit as st
from Pages.principal import principal
from Pages.EDA import a_exploratoria
from Pages.quali import a_qual_dados
from Pages.results import resultados

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', 'Análise exploratória', 'Análise de qualidade de dados', 'Resultado do modelo de regressão linear'])

if menu == 'Principal':
    principal.principal()
elif menu == 'Análise exploratória':
    EDA.a_exploratoria()
elif menu == 'Análise de qualidade de dados':
    quali.a_qual_dados()
elif menu == 'Resultado do modelo de regressão linear':
    results.resultados()
