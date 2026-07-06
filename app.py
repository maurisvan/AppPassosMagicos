import streamlit as st
import pandas as pd
import joblib

# 1. Configuração da Página
st.set_page_config(
    page_title="Predição de Risco - Passos Mágicos",
    page_icon="🪄",
    layout="centered"
)

# 2. Carregar o Modelo Salvo
@st.cache_resource
def carregar_modelo():
    # Carrega o arquivo .pkl que geramos no notebook
    return joblib.load('modelo_risco.pkl')

modelo = carregar_modelo()

# 3. Cabeçalho da Aplicação
st.title("🪄 Portal Preditivo: Passos Mágicos")
st.markdown("""
Esta aplicação utiliza Machine Learning para analisar os indicadores de um aluno e prever a **probabilidade de risco de defasagem**. 
Insira as notas (de 0 a 10) nos campos abaixo para realizar a análise.
""")

st.divider()

# 4. Entradas de Dados (Inputs)
st.subheader("Indicadores do Aluno")

col1, col2, col3 = st.columns(3)

with col1:
    ida = st.number_input("Desempenho (IDA)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    ieg = st.number_input("Engajamento (IEG)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

with col2:
    iaa = st.number_input("Autoavaliação (IAA)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    ips = st.number_input("Psicossocial (IPS)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

with col3:
    ipp = st.number_input("Psicopedagógico (IPP)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    ipv = st.number_input("Ponto de Virada (IPV)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

st.divider()

# 5. Botão de Ação e Previsão
if st.button("Analisar Risco de Defasagem", type="primary"):
    # Organizar os dados exatamente na mesma ordem em que o modelo foi treinado
    dados_entrada = pd.DataFrame([[ida, ieg, iaa, ips, ipp, ipv]], 
                                 columns=['IDA', 'IEG', 'IAA', 'IPS', 'IPP', 'IPV'])
    
    # Fazer a predição
    previsao = modelo.predict(dados_entrada)[0]
    probabilidade = modelo.predict_proba(dados_entrada)[0]
    
    # Exibir o resultado
    st.subheader("Resultado da Avaliação:")
    
    if previsao == 1: # 1 representa Risco (IAN < 10)
        st.error(f"⚠️ **ALERTA DE RISCO DETECTADO**")
        prob_risco = probabilidade[1] * 100
        st.write(f"O modelo indica uma probabilidade de **{prob_risco:.1f}%** de o aluno entrar em defasagem.")
        st.info("Recomendação: Iniciar acompanhamento psicopedagógico e monitorar o engajamento de perto.")
    else: # 0 representa Adequado
        st.success(f"✅ **DESENVOLVIMENTO ADEQUADO**")
        prob_adequado = probabilidade[0] * 100
        st.write(f"O modelo indica que o aluno apresenta baixo risco de defasagem (Confiança: {prob_adequado:.1f}%).")
        st.balloons()