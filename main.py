import streamlit as st
import conexao as tc


st.set_page_config(
    layout = 'wide',
    page_title = 'Projeto IC',
    initial_sidebar_state="auto"
)

st.title('Projeto IC - OMOP')

#Consulta a ser feita na base de dados
import time
campo = st.text_input("Informe o campo da consulta:", key="campo")
consulta = st.text_input("Informe o valor da consulta:", key="consulta")

if st.button("Consultar"):
    bar = st.progress(0)
    st.write("Buscando na base de dados...")
    df = tc.selecionaCriterios(campo, consulta)

    for i in range(100):
        bar.progress(i+1)
        time.sleep(0.01)
    
    st.table(df)

with st.sidebar:
    st.write(
        """
        Projeto de Iniciação Científica\n
        """
    )

