
#Testando conexao com uma database genérica de carros

import pandas as pd
import numpy as np
import pandas.io.sql as psql

from sqlalchemy import create_engine

engine = create_engine('postgresql://rafael:rafael@localhost:5432/mydb') 
connection = engine.connect()

def selecionaCriterios(campoUsuario, valorUsuario):
    query = "SELECT * FROM cars WHERE brand = %(valor)s"
    params={"campo":campoUsuario, "valor":valorUsuario}
    df = psql.read_sql(query, engine, params=params)
    return df

# SELECT * FROM cars WHERE brand = 'Tesla';
# %(campo)s=%(marca)s