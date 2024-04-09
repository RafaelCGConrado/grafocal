import config 
import util
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def eda_tab():

    if config.flag_data_loaded:

        with st.expander(label="Selecione as opções do grafo", expanded=True):
            cc1, cc2, cc3 = st.columns(3)

            with cc1:
                hasSource = st.checkbox(label="Origem", value=True, disabled=True)

            with cc2:
                hasDestination = st.checkbox(label="Destino", value=True, disabled=True)
            
            with cc3:
                hasTimeStamp = st.checkbox(label="Timestamp", value=True, disabled=True)

            c1, c2, c3 = st.columns(3)

            with c1:
                if hasSource:
                    config.opt_source = st.selectbox(label="Origem", options=config.df_query_result.columns, index=min(0, len(config.df_query_result.columns)-1))
                else:
                    config.opt_source = None 
            
            with c2:
                if hasDestination:
                    config.opt_destination = st.selectbox(label="Destino", options=config.df_query_result.columns, index=min(0, len(config.df_query_result.columns)-1))
                else:
                    config.opt_destination = None

            with c3:
                if hasTimeStamp:
                    config.opt_timestamp = st.selectbox(label="TimeStamp", options=config.df_query_result.columns, index=min(0, len(config.df_query_result.columns)-1))
                else:
                    config.opt_timestamp = None

    else:
        st.write("Carregue os dados da consulta!")