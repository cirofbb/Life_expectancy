import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def a_exploratoria():
    # Carregando a base de dados
    try:
        df = pd.read_csv(
            'https://raw.githubusercontent.com/cirofbb/Life_expectancy/main/data/Life-Expectancy-Data-Updated.csv')
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

    # Reorganizando o índice por ordem alfabética de países e anos
    df_novo = df.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    # Criando uma nova variável de status socioeconômico a partir de duas colunas existentes
    df_novo['Economy_status'] = df_novo.apply(
        lambda row: 1 if row['Economy_status_Developed'] == 1 else 0, axis=1)
    df_novo = df_novo.drop(
        ['Economy_status_Developing', 'Economy_status_Developed'], axis=1)

    st.title('1. Análise exploratória')
    st.subheader('Barplot da expectativa de vida por região')
    fig, ax = plt.subplots()
    sns.barplot(x='Region', y='Life_expectancy', data=df_novo)
    plt.title('Expectativa de vida por região')
    plt.xticks(rotation=90)
    plt.figure(figsize=(15, 8))
    st.pyplot(fig)
    st.subheader('Barplot da mortalidade infantil por região')
    fig, ax = plt.subplots()
    sns.barplot(x='Region', y='Infant_deaths', data=df_novo)
    plt.title('Mortalidade infantil por região (mortes por cada mil nascimentos)')
    plt.xticks(rotation=90)
    plt.figure(figsize=(15, 8))
    st.pyplot(fig)
    st.subheader(
        'Barplot da expectativa de vida por região, dividida por status econômico')
    media_expectativa_status = df_novo.groupby(['Region', 'Year', 'Economy_status'])[
        'Life_expectancy'].mean()
    media_expectativa_status = media_expectativa_status.reset_index()
    fig, ax = plt.subplots()
    sns.barplot(x='Region', y='Life_expectancy',
                hue='Economy_status', data=media_expectativa_status)
    plt.title(
        'Média da expectativa de vida por região, divididas por status econômico')
    plt.xticks(rotation=90)
    plt.figure(figsize=(15, 8))
    st.pyplot(fig)
    st.subheader('Heatmap com a correlação entre as variáveis')
    num_col = [
        'Infant_deaths', 'Under_five_deaths', 'Adult_mortality', 'Alcohol_consumption', 'Hepatitis_B', 'Measles',
        'BMI', 'Polio', 'Diphtheria', 'Incidents_HIV', 'GDP_per_capita', 'Population_mln', 'Thinness_ten_nineteen_years',
        'Thinness_five_nine_years', 'Schooling', 'Life_expectancy', 'Economy_status']
    df_numeric = df_novo[num_col]
    corr_matrix = df_numeric.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Mapa de calor da correlação entre as variáveis')
    fig = plt.gcf()
    st.pyplot(fig)
