import config 
import util
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def eda_tab():

    if config.flag_data_loaded:

        with st.expander(label="Selecione as opções do grafo", expanded=True):
            cc1, cc2, cc3, cc4 = st.columns(4)

            with cc1:
                hasSource = st.checkbox(label="Origem", value=True, disabled=True)

            with cc2:
                hasDestination = st.checkbox(label="Destino", value=True, disabled=True)
            
            with cc3:
                hasTimeStamp = st.checkbox(label="Timestamp", value=True, disabled=True)
            
            with cc4:
                hasMeasure = st.checkbox(label="Peso da aresta", value=True, disabled=True)

            c1, c2, c3, c4 = st.columns(4)


            #brand
            with c1:
                if hasSource:
                    config.opt_source = st.selectbox(label="Origem", options=config.df_query_result.columns, index=min(0, len(config.df_query_result.columns)-1))
                else:
                    config.opt_source = None 
            
            #model
            with c2:
                if hasDestination:
                    config.opt_destination = st.selectbox(label="Destino", options=config.df_query_result.columns, index=min(1, len(config.df_query_result.columns)-1))
                else:
                    config.opt_destination = None

            #year
            with c3:
                if hasTimeStamp:
                    config.opt_timestamp = st.selectbox(label="TimeStamp", options=config.df_query_result.columns, index=min(2, len(config.df_query_result.columns)-1))
                else:
                    config.opt_timestamp = None
            
            #frequencia
            with c4:
                if hasMeasure:
                    config.opt_measure = st.selectbox(label="Peso aresta", options=config.df_query_result.columns, index=min(3, len(config.df_query_result.columns)-1))


        form_model_graph = st.form(key="model_graph")
        config.flag_use_prefix_in_graph = form_model_graph.checkbox("Modelar relacionamento entre conceitos",
                                                                    help="Adiciona o nome do atributo como prefixo aos valores modelados",
                                                                    value=True)
        
        graph_construct_submitted = form_model_graph.form_submit_button("Criar grafo", use_container_width=True)

    else:
        st.write("Carregue os dados da consulta!")