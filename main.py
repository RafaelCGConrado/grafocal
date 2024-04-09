import streamlit as st
from dashboard import launch_dashboard

st.set_page_config(
    layout = 'wide',
    page_title = 'Projeto IC',
    initial_sidebar_state="auto"
)

st.title('Projeto IC - OMOP')

with st.sidebar:
    st.write(
        """
        Projeto de Iniciação Científica\n
        """
    )

launch_dashboard()

