import streamlit as st
from dashboard import launch_dashboard

st.set_page_config(
    layout = 'wide',
    page_title = 'GraFOCAL',
    initial_sidebar_state="auto"
)

st.title('GraFOCAL: Graph Features for Common Data Models')

with st.sidebar:
    st.write(
        """
        GraFOCAL\n
        """
    )

launch_dashboard()

