# 🪄 Datathon: Case Passos Mágicos - Previsão de Risco e Análise Educacional

## 📌 Sobre o Projeto
Este repositório contém a solução desenvolvida para a Fase 5 do Datathon, focada na Associação Passos Mágicos, uma ONG com 35 anos de atuação na transformação da vida de crianças e jovens de baixa renda por meio da educação. 

O objetivo principal deste projeto de Data Analytics é extrair insights valiosos sobre o desempenho, engajamento e desenvolvimento psicossocial dos alunos entre 2022 e 2024, além de desenvolver um modelo preditivo em Machine Learning para identificar estudantes em risco de defasagem educacional.

## 🎯 Entregáveis do Projeto
A solução foi dividida nas seguintes frentes, cumprindo os requisitos do desafio:
* **Análise Exploratória de Dados (EDA) e ETL:** Limpeza avançada da base de dados histórica, cruzamento de indicadores:
IAA: Indicador de Autoavaliação (a percepção do próprio aluno sobre si mesmo).
IDA: Indicador de Desempenho (geralmente ligado às notas nas matérias, como Matemática, Português e Inglês).
IEG: Indicador de Engajamento (mede a participação, presença e entrega de atividades).
IPS: Indicador Psicossocial (avalia aspectos sociais, emocionais e familiares do aluno).
IPP: Indicador Psicopedagógico (avaliação do acompanhamento psicológico e pedagógico, que vimos faltar na base de 2022).
IPV: Indicador de Ponto de Virada (métrica que avalia se o aluno atingiu um estágio de desenvolvimento transformador no programa).
IAN: Indicador de Adequação de Nível (mede o "Nível de Defasagem" do aluno em relação à fase/idade ideal escolar, classificando-o em níveis como Adequado, Moderado ou Severo).
Geração de gráficos gerenciais para storytelling.
* **Modelagem Preditiva:** Criação de um modelo de classificação (Random Forest) para prever a probabilidade de um aluno entrar em risco de defasagem.
* **Dashboard Interativo (Deploy):** Desenvolvimento e deploy de uma aplicação web preditiva na Community Cloud utilizando a biblioteca Streamlit.
* **Apresentação Executiva:** Storytelling com os dados, respondendo às dores de negócio e validando a efetividade institucional do programa.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação e Análise de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, Joblib
* **Deploy da Aplicação:** Streamlit (Community Cloud)
* **Link da aplicação:** https://apppaappsmagicos-gjgmj2nsvaxgkzbhsezmpz.streamlit.app/ 

## 🚀 Como executar o projeto localmente

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/maurisvan/AppPassosMagicos.git](https://github.com/maurisvan/AppPassosMagicos.git)
   cd AppPassosMagicos
