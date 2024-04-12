import config
import util 
from data_load import data_load_tab
from eda import eda_tab
import pandas as pd
import streamlit as st

# def update_sidebar():
#     with st.sidebar:
#         opt_connection = st.selectbox(label="Selecione a opção de conexão",
#                                       options=["Local", "Remota"], index = 0)
#         opt_connection = 0 if opt_connection == "Local" else 1
        

def launch_dashboard():

    # update_sidebar()

    tab_data_load, tab_omopcdm, tab_eda = st.tabs(["Carregar Dados", "OMOP-CDM", "EDA"])

    with tab_data_load:
        data_load_tab()
    
    with tab_omopcdm:
        st.write("Nada por enquanto")

    with tab_eda:
        eda_tab()

