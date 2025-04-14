# Life_expectancy
### Dashboard de Análise de Expectativa de Vida
Link para execução do dashboard: https://lifeexpectancy-mv9xy4z8nk867cg5dqqhcz.streamlit.app/

Análise de Expectativa de Vida Global
Este projeto realiza uma análise exploratória de dados sobre expectativa de vida global, incluindo visualizações, análise de qualidade dos dados e um modelo de regressão linear para prever a expectativa de vida com base em diversos fatores socioeconômicos e de saúde.

Visão Geral
O projeto consiste em uma aplicação Streamlit com quatro páginas principais:

Página Principal: Introdução ao projeto

Análise Exploratória: Visualizações dos dados

Análise de Qualidade de Dados: Pré-processamento e normalização

Resultados do Modelo: Regressão linear para prever expectativa de vida

Dados Utilizados
Os dados são provenientes de um arquivo CSV hospedado no GitHub, contendo informações sobre expectativa de vida e diversos indicadores de saúde e socioeconômicos por país e ano.

Link para os dados

Funcionalidades
1. Análise Exploratória
Gráfico de barras da expectativa de vida por região

Gráfico de barras da mortalidade infantil por região

Análise da expectativa de vida por status econômico

Mapa de calor de correlação entre variáveis

2. Análise de Qualidade de Dados
Reorganização dos dados por país e ano

Criação de nova variável de status econômico (0=desenvolvendo, 1=desenvolvido)

Normalização e escalonamento dos dados

3. Modelo de Regressão Linear
Variáveis independentes: Mortalidade infantil, mortalidade adulta, consumo de álcool, vacinação, IMC, HIV, etc.

Variável dependente: Expectativa de vida

Métricas de avaliação: MSE, RMSE e MAE

Visualização das previsões vs valores reais

Como Executar
Certifique-se de ter Python instalado (versão 3.7 ou superior)

Instale as dependências:

Copy
pip install streamlit pandas matplotlib seaborn numpy scikit-learn
Execute o aplicativo:

Copy
streamlit run app.py
Estrutura do Projeto
Copy
.
├── app.py                # Aplicativo principal Streamlit
├── Pages/
│   ├── EDA/
│   │   └── a_exploratoria.py  # Análise exploratória
│   ├── quali/
│   │   └── a_qual_dados.py    # Análise de qualidade
│   └── results/
│       └── resultados.py      # Modelo de regressão
└── README.md             # Este arquivo
Dependências
Python 3.7+

streamlit

pandas

matplotlib

seaborn

numpy

scikit-learn

Resultados do Modelo
O modelo de regressão linear alcançou as seguintes métricas:

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

Os resultados são exibidos na página correspondente do aplicativo.
