import config
import util 
from tab_data_load import data_load_tab
from tab_eda import eda_tab
import pandas as pd
import streamlit as st

def launch_dashboard():
    tab_data_load, tab_eda = st.tabs(["Carregar Dados", "GraFOCAL"])

    with tab_data_load:
        data_load_tab()

    with tab_eda:
        eda_tab()

