import config
import util
import streamlit as st
import pandas as pd

def data_load():

    if(not(config.connection)):
       st.error("Sem conexão com o banco de dados")

    else:
        with st.expander("Carregar dados", expanded=True):
            form_sql_statement = st.form(key='form_sql_statement')

            sql_statement = form_sql_statement.text_area("Consulta (em SQL):", value="SELECT PROGRAMA, AREA_DC, VALOR_TOTAL_DESPACHO_ULT_PROP, DATA_DO_DESPACHO_FINAL FROM SYSTEM.F03")
            sql_submitted = form_sql_statement.form_submit_button("Fazer consulta", use_container_width=True)

            if sql_submitted:
                config.df_query_result = util.run_query(sql_statement)

            if config.df_query_result is not None:
                config.flag_data_loaded = True
                st.dataframe(config.df_query_result.head(), use_container_width=True)
                st.write("Tuplas no dataframe resultante:", len(config.df_query_result))
                st.success("Consulta realizada com sucesso")

                config.df_query_result.to_csv("Resultados_consulta.csv", index=False)
            
            else:
                st.error("Erro ao carregar consulta. Confira o comando SQL informado")