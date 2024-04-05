import sys
import config

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from pyvis.network import Network
import networkx as nx


def run_query(sql_statement):

    try:
        df_query_result = pd.read_sql(sql_statement, con=config.connection)
        print("Consulta realizada com sucesso")

    except Exception as ex:
        print(ex)
        print("Erro ao realizar a consulta")
        df_query_result = None

    return df_query_result